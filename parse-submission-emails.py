#!./.venv/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# python style conventions https://www.python.org/dev/peps/pep-0008/

from typing import List

import shutil  # move
import urllib3
import sys
import email
import json
import os
import argparse
from datetime import datetime
# from email.parser import Parser
from email.utils import mktime_tz, parsedate_tz
# from pprint import pprint
from random import choice
from urllib.parse import parse_qs, urlsplit

# backend
import openapi_client
from openapi_client.api import submissions_api
from openapi_client.model.submission import Submission

# to detect/remove duplicates
usedKeys = set()

# ----------------------------------------------------------------------------

def get_arguments():
    '''parse provided command line arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', help='Authentication token associated with the submit-bot user, generated in the dognews server app', required=True)
    parser.add_argument('--server', help='Where to send the output - use https URL to POST '
                        'to the dognews server API, or a file name to save locally as json',
                        required=True)
    parser.add_argument('--processedfolder', help='Where to move processed eml files', required=True)
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

# -------------------------------------------------------------------------------

def parse_email(startdate, msg) -> List[Submission]:
    date = msg['Date']

    tt = parsedate_tz(date)
    timestamp = mktime_tz(tt)
    msgdate: datetime = datetime.fromtimestamp(timestamp)
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

    return analyse_email(msgdate, contents)


def analyse_email(date: datetime, contents) -> List[Submission]:
    submissions: List[Submission] = []

    submission = None
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
            if target_url in usedKeys:
                # we've seen it already
                continue

            submission = Submission(target_url=target_url[0:199], title=title, description=body, date=date)
            usedKeys.add(target_url)
            submissions.append(submission)
        else:
            body = body + line + ' '

    return submissions

# -------------------------------------------------------------------------------

# DOG NEWS API

def post_articles(server: str, token: str, submissions: List[Submission]):
    configuration = openapi_client.Configuration(
        host = server
    )
    configuration.api_key['tokenAuth'] = token
    configuration.api_key_prefix['tokenAuth'] = 'Token'

    for submission in submissions:
        with openapi_client.ApiClient(configuration) as api_client:
            api_instance =  submissions_api.SubmissionsApi(api_client)

        try:
            print(f'Sending {submission.target_url}')
            api_response = api_instance.submissions_create(submission)
            # pprint(api_response)
            print('    ok')
        except openapi_client.ApiException as e:
            if e.status in [401, 403]:
                print('    %d error code - failed to login' % (e.status))
                print(e.headers)
                print('    make sure the provided token is valid')
                sys.exit(1)
            elif e.status in [400, 500]:
                if 'already exists' in e.body or 'already exists' in e.reason:
                    print('    already exists, ignored')
                    continue
                print('    %d critical error received' % e.status)
                print('    ERROR --->', e.body)
                sys.exit(1)
            else:
                print("Exception when calling SubmissionsApi->submissions_create: %s\n" % e)
        except urllib3.exceptions.MaxRetryError:
            print("ERROR: Cannot connect to server - after retrying.")
            sys.exit(1)



def main(server, token, files, processedfolder):

    startdate = datetime.strptime('17/12/2018', '%d/%m/%Y')

    submissions = []

    # using a maildir folder as input, where email alerts sent by google news
    # are stored in raw format in individual files

    for file_folder in files:
        print(f'Processing: {file_folder}')

        for filename in find_email_files(file_folder):
            print('----- ' + filename)

            with open(filename, 'r') as reader:
                msg = email.message_from_file(reader)

            parsed = parse_email(startdate, msg)
            if parsed:
                # += joins the items flat
                submissions += parsed
                if server.startswith('http'):
                    post_articles(server, token, parsed)
                # mark file as processed
                name = os.path.basename(filename)
                shutil.move(filename, f'{processedfolder}/{name}')

    if not server.startswith('http'):
        # in this case, server is a file name and we dump all at the same time
        with open(server, 'w') as writer:
            writer.write(json.dumps({"submissions": [s.to_dict() for s in submissions]}, indent=2,
                                    sort_keys=True))  # as json


if __name__ == '__main__':
    args = get_arguments()
    main(server=args.server, token=args.token, files=args.files, processedfolder=args.processedfolder)
