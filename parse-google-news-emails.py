#!./venv/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# python style conventions https://www.python.org/dev/peps/pep-0008/

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


def get_arguments():
    '''parse provided command line arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+',
                        help='email filenames and/or directories to traverse '
                        'looking for them')
    return parser.parse_args()


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


# return file name with path - if not found creates 1x1 image and returns that
def get_thumbnail(imageUrl):
    # we want this name to be a hash of the url in case we find it in various
    # darticles or repeated
    hashName = hashlib.md5(imageUrl.encode('utf-8')).hexdigest()
    name = 'images/' + hashName + '.jpg'
    if os.path.isfile(name):
        return name  # we already retrieved this

    try:
        print('  - load image ' + imageUrl + ' [' + hashName + ']')
        r = requests.get(imageUrl, timeout=30, stream=True,
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
        return name

# Parses the actual news article and tries to extract extra info
# returns an object which whatever it found (contents, thumbnail, image, ..)


# Check opengraph protocol meta info (https://ogp.me/)
# <meta property="og:image" content="https://xxxx/xxxx.jpg"/>
def setTagToProp(tags, soup, propName):
    prop = soup.find("meta", property='og:' + propName, content=True)
    if prop:
        tags[propName] = prop.attrs['content']


def generate_extra_tags(hashName, url, title):
    tags = {}

    name = 'scraped/' + hashName + '.html.bz2'
    tags['scraped_html'] = name
    page = None
    if os.path.isfile(name):
        # print(' read ' + url + ' [' + hashName + ']')
        with bz2.open(name, 'rt', encoding='utf-8') as f:
            page = f.read()   # we only keep whatever is read in 1 call
    else:
        try:
            print(' get ' + url)
            r = requests.get(url, timeout=30, headers=random_headers())
            page = r.text
        except Exception:
            page = 'Could not load ' + url + '\n' + traceback.format_exc()
        with bz2.open(name, 'wt', encoding='utf-8') as f:
            f.write(page)

    soup = bs4.BeautifulSoup(page, features='html.parser')

    # Extract opengraph protocol metadata, replace what we have it needed
    for prop in ['image', 'title', 'type', 'url']:
        setTagToProp(tags, soup, prop)

    # very simple attempt at summarising based on
    # https://towardsdatascience.com/easily-scrape-and-summarize-news-articles-using-python-dfc7667d9e74
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
        tags['summary'] = summarize(article, ratio=0.2)
    else:
        tags['summary'] = '\n'.join(sentence_list)

    article_words = article.split()
    if 'title' in tags and tags['title']:
        title = tags['title']  # it may have been overwritten
    if title:
        article_words += title.split()
    if any(badword in article_words for badword in badwords):
        tags['sentiment'] = 'bad'
        if 'ratings' not in tags:
            botRating = {}
            botRating['rating'] = -1
            botRating['date'] = datetime.utcnow().isoformat()
            tags['ratings'] = {'bot': botRating}

    # img = load_image(image)
    # create thumbnail, 512x12
    # convert /tmp/thumb -resize 512 "${thumbname}"
    if 'image' in tags:
        thumbFileName = get_thumbnail(tags['image'])
        if thumbFileName:
            tags['thumbnail'] = thumbFileName

    return tags


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
    url = ''
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
            url = ''
            body = ''
        elif title == '':
            title = line
        elif source == '':
            source = line
        elif line.startswith('<http'):
            url = line[1:-1]
            o = urlsplit(url)
            url = parse_qs(o.query)['url'][0]
            hashName = hashlib.md5(url.encode('utf-8')).hexdigest()
            if hashName in usedKeys:
                continue
            usedKeys.add(hashName)
            data = {}
            dateObj = date_parse(date)
            data['id'] = hashName
            data['date'] = dateObj.isoformat()
            data['fetch_date'] = datetime.utcnow().isoformat()
            data['url'] = url
            data['title'] = title
            data['source'] = source
            data['submitter'] = 'googlenews'
            # note:
            # data['ratings'] =  [{ osuka: { rating: 4, date: xxx },
            #                      pepe: { ... }... ]
            data['body'] = body
            extendedProps = generate_extra_tags(hashName, url, title)
            for prop in extendedProps:
                data[prop] = extendedProps[prop]
            items.append(data)

        else:
            body = body + line + ' '

    return items


def main(files):

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
    with open('extracted-news-items.json', 'w') as writer:
        writer.write(json.dumps(items, indent=2, sort_keys=True))

if __name__ == '__main__':
    args = get_arguments()
    main(args.files)
