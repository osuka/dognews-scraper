#!./.venv/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# python style conventions https://www.python.org/dev/peps/pep-0008/

from typing import List

import sys
import netrc
import email
import hashlib
import json
import bz2
import os
import traceback
import argparse
import urllib3

from datetime import datetime

# beautiful soup 4 (html / xml scraper)
import bs4

# from email.parser import Parser
from email.utils import mktime_tz, parsedate_tz
from pprint import pprint
from random import choice
from urllib.parse import parse_qs, urlsplit

# beautiful soup 4 (html / xml scraper)
import bs4

# http requests
import requests

# date helpers
from dateutil.parser import parse as date_parse

# library to summarise articles
from gensim.summarization import summarize

# pillow - image parsing/generation
from PIL import Image, ImageOps

# marshmallow - serialization
from dataclasses import dataclass, field
from marshmallow import Schema, fields

# backend
import openapi_client
from openapi_client.api.submissions_api import SubmissionsApi
from openapi_client.api.fetchs_api import FetchsApi
from openapi_client.model.fetch_status_enum import FetchStatusEnum
from openapi_client.model.paginated_submission_list import PaginatedSubmissionList
from openapi_client.models import Submission, Fetch

# to detect/remove duplicates
usedKeys = set()

# TODO: Minimal sentiment analysis - using simple word triggers in this version
# https://github.com/linanqiu/word2vec-sentiments
badwords = [
    "die",
    "dies",
    "died",
    "death",
    "mauls",
    "mauling",
    "mauled",
    "kills",
    "killing",
    "killed",
    "horrific",
    "dead",
    "abuse",
    "abused",
    "abusing",
    "brain-damage",
    "brain-damaged",
]

banned_domains = ["www.goal.com", "uk.news.yahoo.com", "uk.sports.yahoo.com", "www.msn.com"]

# notes on https://docs.python.org/3/library/dataclasses.html, they
# automatically generate __init__ and __repr__ (like a 'tostring')


# ----------------------------------------------------------------------------


def get_arguments():
    """parse provided command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        help="Where to send the output - use https URL to POST "
        "to the dognews server API, or a file name to save locally as json",
        default="./extracted-news-items.json",
    )
    parser.add_argument(
        "--token",
        help="Authentication token associated with the submit-bot user, generated in the dognews server app",
        required=True,
    )
    return parser.parse_args()


# -------------------------------------------------------------------------------


def find_submissions(
    submissions_api_instance: SubmissionsApi,
) -> List[Submission]:
    """finds all submissions that haven't been fetched yet"""
    submissions: List[Submission] = []
    try:
        print(f"Retrieving submissions")
        offset = 0
        page_size = 100
        while True:
            api_response: PaginatedSubmissionList = (
                submissions_api_instance.submissions_list(
                    offset=offset, limit=page_size, ordering="-date_created", fetch__status__isnull=True
                )
            )
            submissions = submissions + api_response.results
            offset += len(api_response.results)
            if not api_response.next:
                break
    except openapi_client.ApiException as e:
        if e.status in [401, 403]:
            print("    %d error code - failed to login" % (e.status))
            print(e.headers)
            print("    make sure the provided token is valid")
            sys.exit(1)
        elif e.status in [400, 500]:
            print("    %d critical error received" % e.status)
            print("    ERROR --->", e.body)
            sys.exit(1)
        else:
            print("Exception when calling SubmissionsApi->submissions_list: %s\n" % e)
    except urllib3.exceptions.MaxRetryError:
        print("ERROR: Cannot connect to server - after retrying.")
        sys.exit(1)

    return submissions


def remove_escapes(s):
    s = s.replace("\\'", "'")
    s = s.replace(r"/\\\\x??/", "")
    return s


# Use different user agents to avoid banning
# https://edmundmartin.com/random-user-agent-requests-python/
desktop_agents = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
    + "(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
    + "(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    + "(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 "
    + "(KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
    + "(KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 "
    + "(KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 "
    + "(KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
    + "(KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
    + "(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) " + "Gecko/20100101 Firefox/50.0",
]


def random_headers():
    return {
        "User-Agent": choice(desktop_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;"
        + "q=0.9,image/webp,*/*;q=0.8",
    }


# -------------------------------------------------------------------------------

def generate_thumbnail(image_url:str, fetchobj:Fetch):
    '''
    Creates a thumbnail for the image pointed by the URL - if it can't be loaded
    a 1x1 image used. The thumbnail reference is stored in the news item instance

    It caches images downloaded as they can be referred to from multiple places
    The cache IDs are based on the URL of the image
    '''
    if not image_url:
        return

    hashName = hashlib.md5(image_url.encode('utf-8')).hexdigest()
    name = 'images/' + hashName + '.jpg'
    if os.path.isfile(name):
        fetchobj["thumbnail"] = f'https://dognewsserver.gatillos.com/media/uploads/{name}'
        return

    try:
        print('  - load image ' + image_url + ' [' + hashName + ']')
        r = requests.get(image_url, timeout=30, stream=True,
                         headers=random_headers())
        if r.status_code == 200:
            img = Image.open(r.raw)
            img = img.convert('RGB')
            print('     thumb')
            new_img = ImageOps.fit(img, (512, 512), Image.ANTIALIAS)
            print('     save ' + name)
            new_img.save(name, format='JPEG', quality=85)
        else:
            new_img = Image.new('RGB', (1, 1))
            new_img.save(name, format='JPEG', quality=96)
    except:
        print('       bad image')
        # we save something so it doesn't keep retrying
        new_img = Image.new('RGB', (1, 1))
        new_img.save(name, format='JPEG', quality=96)
    finally:
        fetchobj["thumbnail"] = f'https://dognewsserver.gatillos.com/static/{name}'

# -------------------------------------------------------------------------------

def fill_in_opengraph_properties(fetchobj:Fetch, soup):
    '''
    Receives a beautiful soup instance and looks in it for open graph properties
    to be added to the news item
    * Check opengraph protocol meta info (https://ogp.me/)
    * In HTML props look like: <meta property="og:image" content="https://xxxx/xxxx.jpg"/>
    '''
    print("   checking opengraph entries")
    for prop in ['image', 'title', 'type', 'url', "description"]:
        entry = soup.find("meta", property='og:' + prop, content=True)
        if entry:
            # print(f"   found {entry}")
            value = entry.attrs['content']
            if prop == 'url':
                pass
            elif prop == "image":
                # TODO: Re-enable, maybe separate?
                # generate_thumbnail(value, fetchobj)
                fetchobj["thumbnail"] = value
                pass
            elif prop == "title":
                fetchobj["title"] = value
                print(f"     got title={value}")
            elif prop == "description":
                fetchobj["description"] = value
                print(f"     got description={value}")
# -------------------------------------------------------------------------------

def summarise_article(soup) -> str:
    '''
    Creates a summary of an html page (passed in as a BeautifulSoup instance) and returns it.
    * If the contents is too small, it will simply be added as is
    * Currently it's a very simple attempt at summarising based on
     https://towardsdatascience.com/easily-scrape-and-summarize-news-articles-using-python-dfc7667d9e74
    '''
    all_p = soup.find_all('p')
    all_p_text = [node.get_text().lower().strip() for node in all_p]
    # Filter out sentences that are probably not sentences
    sentence_list = [
        sentence for sentence in all_p_text if 'login' not in sentence]
    sentence_list = [
        sentence for sentence in sentence_list if 'subscribe' not in sentence]
    sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
    # Combine list items into string.
    article = ' '.join(sentence_list)
    summary = ""
    if len(sentence_list) > 3:
        # ratio is how many lines vs the original article to return
        summary = summarize(article, ratio=0.2)
    else:
        summary = '\n'.join(sentence_list)
    if len(summary) > 4000:
        summary = summary[:4000]
    return summary

# -------------------------------------------------------------------------------

def scrape_submission(submission: Submission, submission_api: SubmissionsApi, fetch_api:FetchsApi):
    """
    Parses the actual news article and tries to extract extra info
    Anything discovered is added as properties to the object
    """
    if any(badword in submission.target_url.split("/") for badword in banned_domains):
        submission_api.submissions_fetch_update(submission_id=submission.id, fetch=Fetch(
            status=FetchStatusEnum("rej_fetch"),  # noqa: E501
        ))
        print("   -> bad domain ")
    else:
        try:
            fetched_page = load_article(submission)
            soup = bs4.BeautifulSoup(fetched_page, features='html.parser')
            summary = summarise_article(soup)
            # TODO: use return values
            fetchobj:Fetch = Fetch(
                status=FetchStatusEnum("fetched"),  # noqa: E501
                # title='title',  # noqa: E501
                # description='description',  # noqa: E501
                # thumbnail='thumbnail',  # noqa: E501
                # thumbnail_image='thumbnail_image',  # noqa: E501
                fetched_page=summary,  # noqa: E501
            )
            fill_in_opengraph_properties(fetchobj, soup)
            submission_api.submissions_fetch_update(submission_id=submission.id, fetch=fetchobj)
        except Exception:
            # TODO: reject only on permanent errors
            submission_api.submissions_fetch_update(submission_id=submission.id, fetch=Fetch(
                status=FetchStatusEnum("rej_error"),  # noqa: E501
            ))
            print("   -> read error ")
            return

    print("   -> read ok -> accepted")


def load_article(submission):
    """
    Loads the contents of the url
    """
    page_contents = None
    print(" get " + submission.target_url)
    r = requests.get(submission.target_url, timeout=30, headers=random_headers())
    page_contents = r.text
    return page_contents


# -------------------------------------------------------------------------------


def main(server, authToken):

    configuration = openapi_client.Configuration(host=server)
    configuration.api_key["tokenAuth"] = authToken
    configuration.api_key_prefix["tokenAuth"] = "Token"

    with openapi_client.ApiClient(configuration) as api_client:
        submissions_api_instance = SubmissionsApi(api_client)
        fetch_api_instance = FetchsApi(api_client)

    submissions: List[Submission] = find_submissions(submissions_api_instance)
    for submission in submissions:
        print(submission.status, submission.target_url, submission.title)
        if hasattr(submission, "fetch"):
            print("already processed")
        scrape_submission(
            submission=submission,
            submission_api=submissions_api_instance,
            fetch_api=fetch_api_instance
        )


if __name__ == "__main__":
    args = get_arguments()
    main(server=args.output, authToken=args.token)
