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

This is a very simple project: use virtualenv to generate a python3 based environment, pip install -r requirements.txt and run the script. You will need to provide raw email messages as received from google news to test it.

Recommended setup: if you have docker available (even in a remote machine), I highly recommend using [Visual Studio Code Containers](./README-VSC-Container.md). This allows you to have an isolated environment to work on this, and you can use VSC's terminal to run it in an isolated way. When ran in this way, Visual Studio will have the required dependencies for python editing.

## Running

Simply run the `parse-google-news-emails.py` script.

* The script scans all files with extension .eml and treats them as raw, uncompressed, unencrypted mail files (use a poller to get them)
* It parses all of the ones that contain google news, fetching all the links, summarising them and caching the contents, plus generating thumbnails
* Thumbnails are stored in `images/` so they don't have to be re-created
* Cached contents is stored in the folder `scraped/` (this helps for re-runs, but also it's not uncommon to see the same link multiple times)
* Both of these folders are safe to clear at any time
* Processed files are moved to `processed/`
