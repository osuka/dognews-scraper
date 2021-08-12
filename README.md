# Extracting and parsing news articles

This is a collection of scripts / tools to generate content for the website [only dog news](https://onlydognews.com), a simple news aggregator that collates information from different sources and publishes filtered news about dogs (trying to publish only 'nice' news).

## Goal

The idea behind this is to help decide what to post on the site, which is just a side project and for which I don't have a lot of time. The current process involves basically trawling the news manually, finding interesting stuff and flagging it.

This will continue as is but as an experiment I wanted to add some automation based on Google News Alerts. In Google News you can define keywords and receive a summary email with articles that contain them. For generic words like 'dog' there are way too many articles so we need some kind of filtering.

There's a few problems with stopping just there:

* Google News does a decent job but it has different goals to what we have here: google wants to make money. I want nice/interesting dog news.
* Clicking on google news articles gets dangerous: News sites are notoriously spammy and in fact one of the reasons to have a simple aggregator was to share nice news while avoiding repetitive and content-less articles. Some of the sites show a lot of ads, including auto playing videos etc. To prevent going crazy and at the same time getting a feel of what the 'first time visitor' experience is, while browsing we need to open them always in private mode. A site that is virtually unreadable on a first visit needs to be rejected.
* Summarising the articles: a lot of sites these days include descriptions specifically for this purpose, following the opengraph standard. When browsing manually one has to copy & paste.
* Filtering: there is a lot of time wasted doing this manually. Contrary to popular belief, most of the news articles are pretty horrible (dogs killed / killing, abused, fighting...), and also a lot of sites will wrap a 2-line article into a whole page so they can fit ads.

The ultimate goal is to have these script perform some decent summarising and sentiment analysis on it.

This is the first release that does a decent job but reduces sentiment analysis to finding trigger words.

The news articles parsed are aggregated into a json structure fed into the backend and consumed by a mobile client so that the final step is always manual - I don't want to automate the whole thing, just making the Editors life easier. Users of the mobile app act as moderators and can see a summary of the news article, an initial rating and whether the article was filtered out by the system. At this stage, this very simple analysis and text summarising seems to do enough.

Currently Uses:

* Beautiful Soup 4 to scrape html
* gensim to summarise news articles
* pillow to generate thumbnails

## Setup

This is a very simple project: use virtualenv to generate a python3.7 based environment, pip install -r requirements.txt and run the script. You will need to provide raw email messages as received from google news to test it.

Recommended setup: if you have docker available (even in a remote machine), I highly recommend using [Visual Studio Code Containers](./README-VSC-Container.md). This allows you to have an isolated environment to work on this, and you can use VSC's terminal to run it in an isolated way. When ran in this way, Visual Studio will have the required dependencies for python editing.

## Running

Simply run the `parse-google-news-emails.py` script.

* The script scans all files with extension .eml and treats them as raw, uncompressed, unencrypted mail files (use a poller to get them)
* It parses all of the ones that contain google news, fetching all the links, summarising them and caching the contents, plus generating thumbnails
* Thumbnails are stored in `images/` so they don't have to be re-created
* Cached contents is stored in the folder `scraped/` (this helps for re-runs, but also it's not uncommon to see the same link multiple times)
* Both of these folders are safe to clear at any time
* Processed files are moved to `processed/`

## DEV notes

Creating the API client. We are using a django rest framework based API that exposes an OpenAPI 3.0 schema and we explore a couple of ways to automatically generate a client:

### Generating using the openapi-generator

This is a nodejs wrapper of the multi-language generator [openapi-generator](https://github.com/OpenAPITools/openapi-generator) that makes running it a lot easier.

Check the [generator documentation](https://github.com/openapitools/openapi-generator-cli) for instructions on how to use these kind of clients.

You can check [the list of generators](https://github.com/OpenAPITools/openapi-generator/blob/master/docs/generators/). For python it creates clients but can also create a variety of servers (which we don't need but good to know).
* python-aiohttp (generates a server app using the async io http library aiohttp)
* python-fastapi.md (generates a server app using fastapi)
* python-blueplanet.md (generates a server app for blueplanet, whatever that is)
* python-flask.md (generates a server app in flask, including models etc)
* python.md (generates a client that uses urllib, asyncio or tornado)
* python-legacy.md (generates a client that uses urllib3 but uses six for python2 compatibility)

Those documents contain the possible parameters. We are using the default [`python`](https://github.com/OpenAPITools/openapi-generator/blob/master/docs/generators/python.md) generator. We will use these two:

* generateSourceCodeOnly: otherwise it creates a full python package with setup scripts, tests etc
* library: asyncio, tornado, urllib3

```bash
❯ npx @openapitools/openapi-generator-cli generate -i ../dognews-server/openapi-schema.yml -g python -o . --additional-properties=generateSourceCodeOnly=true,library=urllib3
```

This creates:

```text
openapi_client/  folder with models, client etc
.openapi-generator/  folder with a kind of manifest of all that is created (FILES, VERSION)
.openapi-generator-ignore  file where we can declare names of files we don't want the generator to override
openapi_client_README.md  explains how to use the library
```

The [generated readme](./openapi_client_README.md) contains excellent docs on how to use it.

### Generating using openapi-python-client

This is a library aiming to solve some of the issues from the generic `openapi-generator` approach: namely usage of python-specific modern features.

The documentation is at [openapi-python-client](https://pypi.org/project/openapi-python-client/).

```bash
❯ openapi-python-client generate --url http://localhost:8000/api/schema/ --meta none
Generating dognews-server-api-client
```

> --meta-none prevents it from creating a folder with [poetry](https://python-poetry.org/) configuration since we just want it as a local python module
