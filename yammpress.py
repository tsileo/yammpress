# -*- encoding: utf-8 -*-
from datetime import datetime
import codecs
import os.path
import logging
import glob

from markdown2 import markdown
from dateutil.parser import parse
from slugify import slugify # python-slugify
from pymongo import Connection
import yaml
from komandr import command, main as kmain

EXCERPT_SEPARATOR = "<!--more-->"
REQUIRED_METADATAS = ["title", "date"]
MARKDOWN_EXTRAS = ["metadata", "fenced-code-blocks"]

BLANK_post = u"""---
title: {title}
date: {date}
---

excerpt

{excerpt_separator}

content

"""

DEFAULT_CONF = {"mongo_host": "localhost:27017",
                "mongo_db": "yammpress",
                "mongo_collection": "posts"}


log = logging.getLogger(__name__)

if not log.handlers:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


def get_conf(config_file="yammpress.yml"):
    user_conf = DEFAULT_CONF.copy()
    if os.path.isfile(config_file):
        with open(config_file, "r") as f:
            user_conf.update(yaml.load(f))
    return user_conf

def get_col(conf=get_conf()):
    con = Connection(conf["mongo_host"])
    return con[conf["mongo_db"]][conf["mongo_collection"]]

@command
def new_post(title):
    """
    """
    title = title.decode("utf-8")
    post_data = dict(slug=slugify(title),
                        title=title,
                        date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        excerpt_separator=EXCERPT_SEPARATOR)

    filename = post_data["slug"] + ".md"
    if os.path.isfile(filename):
        raise Exception(filename + " already exists")

    with codecs.open(filename, "w", "utf-8") as f:
        f.write(BLANK_post.format(**post_data))


def open_post(filename):
    """
    Parse markdown file with metadatas, 
    also try to extract excerpt.
    """
    raw = open(filename).read()
    html = markdown(raw, extras=MARKDOWN_EXTRAS)

    metadata = dict(html.metadata)
    
    excerpt = None
    
    if EXCERPT_SEPARATOR in html:
        excerpt, html = html.split(EXCERPT_SEPARATOR)

    for key in REQUIRED_METADATAS:
        if not key in metadata:
            raise Exception("No {} metadata".format(key))

    title = metadata["title"]
    del metadata["title"]

    try:
        metadata["date"] = parse(metadata["date"])

        if "updated" in metadata:
            metadata["updated"] = parse(metadata["updated"])
    
    except ValueError:
        raise Exception("Unknow date format in metadata")

    return dict(title=title, metadata=metadata, html=html, excerpt=excerpt, slug=filename[:-3])

@command
def status():
    log.info("STATUS:")
    conf = get_conf()
    col = get_col(conf)
    log.info("Configuration:")
    log.info(conf)
    log.info("Stats:")
    log.info(str(col.count()) + " posts")

@command
def generate():
    log.info("GENERATE:")
    col = get_col()
    for md_filename in glob.glob("*.md"):
        log.info(md_filename)
        post = open_post(md_filename)
        col.update({"slug": md_filename[:-3]}, post, upsert=True)
        log.info("=> OK")

@command
def drop():
    log.info("DROP:")
    col = get_col()
    col.drop()
    log.info("OK")


class YammPress:
    def __init__(self, col=None):
        if not col:
            con = Connection(DEFAULT_CONF["mongo_host"])
            col = con[DEFAULT_CONF["mongo_db"]][DEFAULT_CONF["mongo_collection"]]
        self.col = col
        self.cursor = col.find().sort("metadata.date", -1)

    def get_posts(self, skip=0, limit=10):
        return self.cursor.skip(skip).limit(limit)

    def get_all(self):
        return self.cursor

    def get_by_slug(self, slug):
        return self.col.find_one({"slug": slug})

    def count(self):
        return len(self)


    def __len__(self):
        return self.col.count()

def main():
    kmain()

if __name__ == "__main__":
    main()