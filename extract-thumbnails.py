#!./.venv/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# python style conventions https://www.python.org/dev/peps/pep-0008/

from openapi_client.model.patched_fetch import PatchedFetch
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

# from email.parser import Parser
from email.utils import mktime_tz, parsedate_tz
from pprint import pprint
from random import choice
from urllib.parse import parse_qs, urlsplit

# http requests
import requests

# date helpers
from dateutil.parser import parse as date_parse

# pillow - image parsing/generation
from PIL import Image, ImageOps

# backend
import openapi_client
from openapi_client.api.submissions_api import SubmissionsApi
from openapi_client.api.fetchs_api import FetchsApi
from openapi_client.model.fetch_status_enum import FetchStatusEnum
from openapi_client.model.paginated_submission_list import PaginatedSubmissionList
from openapi_client.models import Submission, Fetch

# ----------------------------------------------------------------------------


def get_arguments():
    """parse provided command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--server",
        help="Where to send the output - use https URL to POST "
        "to the dognews server API, or a file name to save locally as json",
        required=True)
    parser.add_argument(
        "--imagefolder",
        help="Where to save the thumbnails",
        required=True)
    parser.add_argument(
        "--token",
        help="Authentication token associated with the submit-bot user, generated in the dognews server app",
        required=True)
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
                    offset=offset,
                    limit=page_size,
                    ordering="-date_created",
                    fetch__status="fetched",
                    fetch__thumbnail__isnull=False,
                    fetch__generated_thumbnail__isnull=True,
                )
            )
            submissions = submissions + api_response.results
            offset += len(api_response.results)
            if not api_response.next:
                break
            break  # TODO: REMOVE
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


def generate_thumbnail(imagefolder:str, fetchobj: Fetch) -> str:
    """
    Creates a thumbnail for the image pointed by the URL - if it can't be loaded
    a 1x1 image used. The final thumbnail URL is returned.

    It caches images downloaded as they can be referred to from multiple places
    The cache IDs are based on the URL of the image
    """
    if not hasattr(fetchobj, "thumbnail"):
        # TODO: we could still look for other images
        return None

    hashName = hashlib.md5(fetchobj.thumbnail.encode("utf-8")).hexdigest()

    if imagefolder == None:
        print(f"Error, image folder is set to {imagefolder}")
        return None

    # they are saved to a local folder called 'images'
    dest = imagefolder
    name = f"images/" + hashName + ".jpg"
    if os.path.isfile(f"{dest}/{name}"):
        return f"{name}"

    try:
        print("  - load image " + fetchobj.thumbnail + " [" + hashName + "]")
        r = requests.get(
            fetchobj.thumbnail, timeout=30, stream=True, headers=random_headers()
        )
        if r.status_code == 200:
            img = Image.open(r.raw)
            img = img.convert("RGB")
            print("     thumb")
            new_img = ImageOps.fit(img, (512, 512), Image.ANTIALIAS)
            print(f"     save {dest}/{name}")
            new_img.save(f"{dest}/{name}", format="JPEG", quality=85)
        else:
            new_img = Image.new("RGB", (1, 1))
            new_img.save(f"{dest}/{name}", format="JPEG", quality=96)
    except:
        print("       bad image")
        # we save something so it doesn't keep retrying
        new_img = Image.new("RGB", (1, 1))
        new_img.save(f"{dest}/{name}", format="JPEG", quality=96)
    finally:
        return f"{name}"


# -------------------------------------------------------------------------------


def main(server: str, imagefolder: str, authToken:str):

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
            print(f"  - retrieving {submission.fetch}")
            fetchobj: Fetch = fetch_api_instance.fetchs_retrieve(submission.id)
            if hasattr(fetchobj, "generated_thumbnail"):
                previous = fetchobj.generated_thumbnail
            else:
                previous = None
            print(f"  - generating {submission.id} to save in {imagefolder}")
            new_image = generate_thumbnail(imagefolder, fetchobj)
            patchedfetch: PatchedFetch = PatchedFetch(generated_thumbnail=new_image)
            if previous != new_image:
                print(f"  - saving {submission.id} with {patchedfetch.generated_thumbnail}")
                fetch_api_instance.fetchs_partial_update(submission.id, patched_fetch=patchedfetch)


if __name__ == "__main__":
    args = get_arguments()
    main(server=args.server, imagefolder=args.imagefolder, authToken=args.token)
