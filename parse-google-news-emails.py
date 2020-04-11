#!./venv/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# python style conventions https://www.python.org/dev/peps/pep-0008/

import sys
import netrc
import email
import hashlib
import json
import bz2
import os
import traceback
import argparse
from datetime import datetime
# from email.parser import Parser
from email.utils import mktime_tz, parsedate_tz
# from pprint import pprint
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

# to detect/remove duplicates
usedKeys = set()

# TODO: Minimal sentiment analysis - using simple word triggers in this version
# https://github.com/linanqiu/word2vec-sentiments
badwords = [
    'die', 'dies', 'died', 'death',
    'mauls', 'mauling', 'mauled',
    'kills', 'killing', 'killed',
    'horrific', 'dead',
    'abuse', 'abused', 'abusing',
    'brain-damage', 'brain-damaged',
]

banned_domains = [
]

# notes on https://docs.python.org/3/library/dataclasses.html, they
# automatically generate __init__ and __repr__ (like a 'tostring')


@dataclass
class NewsItemRating:
    rating: int
    date: datetime = datetime.utcnow()


class NewsItemRatingSchema(Schema):
    # user = fields.String()  auto generated
    rating = fields.Integer()
    date = fields.DateTime()


@dataclass
class NewsItem:
    # internal fields
    id: str = field(init=False)

    # mandatory fields
    target_url: str
    date: datetime
    title: str
    source: str
    submitter: str
    ratings: list = field(default_factory=list)

    fetch_date: datetime = datetime.utcnow()

    # stubs for properties that come from OpenGraph
    image: str = None
    type: str = None

    # calculated properties
    body: str = None   # small description, either manual or coming from google news or og

    cached_page: str = None  # local file name where the scraped HTML is saved
    thumbnail: str = None  # local file name of a generated thumbnail

    summary: str = None
    sentiment: str = None   # sentiment currently is empty or 'bad'

    def __post_init__(self):
        self.generate_id()

    def generate_id(self):   # generates the id field, from the url
        self.id = hashlib.md5(self.target_url.encode('utf-8')).hexdigest()

    def set_url(self, target_url):
        self.target_url = target_url
        self.generate_id()

    def set_og_prop(self, prop_name, prop_value):
        # props that come directly from the opengraph standard
        # we only store a few
        if prop_name == 'image':
            self.image = prop_value
        elif prop_name == 'title':
            self.title = prop_value
        elif prop_name == 'type':
            self.type = prop_value
        elif prop_name == 'url':
            self.set_url(prop_value)

    def add_rating(self, rating):
        # rating is a Rating instance
        assert(isinstance(rating, NewsItemRating))
        self.ratings.append(rating)


class NewsItemSchema(Schema):
    id = fields.String()
    target_url = fields.String()
    date = fields.DateTime()
    title = fields.String()
    source = fields.String()
    submitter = fields.String()
    ratings = fields.List(fields.Nested(NewsItemRatingSchema))
    fetch_date = fields.DateTime()
    image = fields.String()
    type = fields.String()
    body = fields.String()
    cached_page = fields.String()
    thumbnail = fields.String()
    summary = fields.String()
    sentiment = fields.String()


class NewsItemListSchema(Schema):
    items = fields.List(fields.Nested(NewsItemSchema))


# ----------------------------------------------------------------------------


def get_arguments():
    '''parse provided command line arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', help='Where to send the output - use https URL to POST '
                        'to the dognews server API, or a file name to save locally as json',
                        default='./extracted-news-items.json')
    parser.add_argument('files', nargs='+',
                        help='email filenames and/or directories to traverse '
                        'looking for them')
    return parser.parse_args()

# -------------------------------------------------------------------------------


def find_email_files(root):
    '''finds all raw email files from a directory - accepts also file names
    '''
    if os.path.isfile(root):
        if root.endswith('.eml'):
            yield root
        else:
            print(f'{root}: not an eml file')
        return

    for (dirpath, _, files) in os.walk(root):
        for fileName in files:
            if fileName.endswith('.eml'):
                yield os.path.join(dirpath, fileName)
            else:
                print(f'{fileName}: not an eml file')


def remove_escapes(s):
    s = s.replace("\\'", "'")
    s = s.replace(r"/\\\\x??/", "")
    return s


# Use different user agents to avoid banning
# https://edmundmartin.com/random-user-agent-requests-python/
desktop_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ' +
    '(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' +
    '(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
    '(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 ' +
    '(KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' +
    '(KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 ' +
    '(KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 ' +
    '(KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ' +
    '(KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ' +
    '(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) ' +
    'Gecko/20100101 Firefox/50.0'
]


def random_headers():
    return {'User-Agent': choice(desktop_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;' +
            'q=0.9,image/webp,*/*;q=0.8'
            }

# -------------------------------------------------------------------------------


def scrape_item(item):
    '''
        Parses the actual news article and tries to extract extra info
        Anything discovered is added as properties to the item object
    '''
    page_contents = load_article(item)
    soup = bs4.BeautifulSoup(page_contents, features='html.parser')
    fill_in_opengraph_properties(item, soup)
    summarise_article(item, soup)
    sentiment_analysis(item)
    generate_thumbnail(item)


def generate_thumbnail(item):
    '''
    Creates a thumbnail for the image pointed by the URL - if it can't be loaded
    a 1x1 image used. The thumbnail reference is stored in the news item instance

    It caches images downloaded as they can be referred to from multiple places
    The cache IDs are based on the URL of the image
    '''
    if not item.image:
        return

    hashName = hashlib.md5(item.image.encode('utf-8')).hexdigest()
    name = 'images/' + hashName + '.jpg'
    if os.path.isfile(name):
        item.thumbnail = name
        return

    try:
        print('  - load image ' + item.image + ' [' + hashName + ']')
        r = requests.get(item.image, timeout=30, stream=True,
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
        item.thumbnail = name


def fill_in_opengraph_properties(item, soup):
    '''
    Receives a beautiful soup instance and looks in it for open graph properties
    to be added to the news item
    * Check opengraph protocol meta info (https://ogp.me/)
    * In HTML props look like: <meta property="og:image" content="https://xxxx/xxxx.jpg"/>
    '''
    for prop in ['image', 'title', 'type', 'url']:
        value = soup.find("meta", property='og:' + prop, content=True)
        if value:
            if prop == 'url':
                prop = 'target_url'
            item.set_og_prop(prop, value.attrs['content'])


def summarise_article(item, soup):
    '''
    Creates a summary of an html page (passed in as a BeautifulSoup instance) and stores it into
    the item instance provided.
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
    if len(sentence_list) > 3:
        # ratio is how many lines vs the original article to return
        item.summary = summarize(article, ratio=0.2)
    else:
        item.summary = '\n'.join(sentence_list)

    if len(item.summary) > 4000:
        item.summary = item.summary[:4000]

def sentiment_analysis(item):
    '''
    Placeholder for propert sentiment analysis. Currently it's a simple word search
    '''
    article_words = item.summary.split()
    if item.title:
        article_words += item.title.split()
    if any(badword in article_words for badword in badwords):
        item.sentiment = 'bad'
        item.add_rating(NewsItemRating(-1))  # bot disapproves

    # we search also inside aiming to detect references like google amp's
    # 'https://www.google.com/amp/www.example.com/amp.doc.html'
    if any(badword in item.target_url.split('/') for badword in banned_domains):
        item.sentiment = 'bad'
        item.add_rating(NewsItemRating(-1))  # bot disapproves


def load_article(item):
    '''
    Loads the url of an article for parsing, and caches it so it's only
    fetched if it hasn't been fetched before. A reference to the
    cached location is stored on the item instance.
    '''
    name = 'scraped/' + item.id + '.html.bz2'
    item.cached_page = name
    page_contents = None
    if os.path.isfile(name):
        # print(' read cached ' + target_url + ' [' + hashName + ']')
        with bz2.open(name, 'rt', encoding='utf-8') as f:
            page_contents = f.read()   # we only keep whatever is read in 1 call
    else:
        try:
            print(' get ' + item.target_url)
            r = requests.get(item.target_url, timeout=30, headers=random_headers())
            page_contents = r.text
        except Exception:
            page_contents = 'Could not load ' + item.target_url + '\n' + traceback.format_exc()
        with bz2.open(name, 'wt', encoding='utf-8') as f:
            f.write(page_contents)

    return page_contents

# -------------------------------------------------------------------------------


def parse_email(startdate, msg):
    date = msg['Date']

    tt = parsedate_tz(date)
    timestamp = mktime_tz(tt)
    msgdate = datetime.fromtimestamp(timestamp)
    if startdate > msgdate:
        return

    contents = ''
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))
            if ctype == 'text/plain' and 'attachment' not in cdispo:
                contents = part.get_payload(decode=True)
                break
    else:
        contents = msg.get_payload(decode=True)

    return analyse_email(date, contents)


def analyse_email(date, contents):
    items = []

    title = ''
    source = ''
    target_url = ''
    body = ''
    for line in str(contents).replace('\\r', '').split('\\n'):
        line = remove_escapes(line)
        if '=== News' in line:
            continue
        if line.startswith('- - - -'):
            # no more
            break
        elif line == '':
            title = ''
            source = ''
            target_url = ''
            body = ''
        elif title == '':
            title = line
        elif source == '':
            source = line
        elif line.startswith('<http'):
            target_url = line[1:-1]
            o = urlsplit(target_url)
            target_url = parse_qs(o.query)['url'][0]

            # we have a full object
            datetimeObj = date_parse(date)
            item = NewsItem(target_url=target_url, date=datetimeObj, title=title,
                            source=source, submitter='googlenews')
            if item.id in usedKeys:
                # we've seen this exact article before
                continue
            usedKeys.add(item.id)
            item.body = body
            scrape_item(item)
            items.append(item)

        else:
            body = body + line + ' '

    return items

# -------------------------------------------------------------------------------

# DOG NEWS API

def post_articles(server, items):
    for item in items:
        itemJson = NewsItemSchema().dump(item)

        print('  - Posting %s' % item.title)
        # print(itemJson)
        r = requests.post('%s/newsItem/' % server, timeout=30, json=itemJson)
        if r.status_code in [401, 403]:
            print('    %d error code - failed to login' % (r.status_code))
            print(r.request.headers)
            print('    make sure to define a .netrc file with credentials like:')
            print('    (check https://ec.haxx.se/usingcurl/usingcurl-netrc)')
            print('''
                machine yourserver.com
                login yourusername
                password yourpassword
                ''')
            # Attempt to open it, this will usually raise an exception, like invalid format etc
            if netrc.netrc():
                print('   you seem to have a netrc valid file, may be missing the domain')
            sys.exit()
        elif r.status_code in [400, 500]:
            if 'already exists' in r.text:
                print('    already exists, ignored')
                continue
            print('    %d critical error received' % r.status_code)
            print(r.request.body)
            print('    ERROR --->', r.text)
            sys.exit()
        elif r.status_code not in [200, 201]:
            print('    %d error' % (r.status_code))
        else:
            print('    ok')


def main(output, files):

    startdate = datetime.strptime('17/12/2018', '%d/%m/%Y')

    # TODO: local db instead of json file (?)
    # db = sqlite3.connect('news-database.db')
    # db.execute('''
    # CREATE TABLE news )

    items = []

    # using a maildir folder as input, where email alerts sent by google news
    # are stored in raw format in individual files

    for file_folder in files:
        print(f'Processing: {file_folder}')

        for filename in find_email_files(file_folder):
            print('----- ' + filename)

            # with open(filename, 'r') as reader:
            #     headers = Parser().parse(reader)

            with open(filename, 'r') as reader:
                msg = email.message_from_file(reader)

            parsed = parse_email(startdate, msg)
            if parsed:
                # += joins the items flat
                items += parsed
                # mark file as processed
                name = os.path.basename(filename)
                os.rename(filename, f'./processed/{name}')

    # uploading is done by a separate process
    if not output.startswith('http'):
        # in this case, server is a file name
        with open(output, 'w') as writer:
            serialized = NewsItemListSchema().dump(
                {"items": items})  # as object using base python types
            writer.write(json.dumps(serialized, indent=2,
                                    sort_keys=True))  # as json
    else:
        post_articles(output, items)


if __name__ == '__main__':
    args = get_arguments()
    main(output=args.output, files=args.files)
