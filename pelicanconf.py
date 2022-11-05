#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import datetime

AUTHOR = "MM"
SITENAME = "CODEC UCL"
SITEURL = ''
SITEDESCRIPTION = "UCL CODEC and related Projects"
SITELOGO = "/images/CODEC.jpg"
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"
COPYRIGHT_YEAR = datetime.date.today().year
TIMEZONE = "Europe/London"
DEFAULT_LANG = "en"

PATH = "content"
STATIC_PATHS = [
    "extra","images",
    ]

EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    }

# Creative Commons Licensing
CC_LICENSE = {
        'name': 'Creative Commons Attribution-ShareAlike',
        'version': '4.0',
        'slug': 'by-sa'
}

# Theme
THEME = "extra/pelican-themes/flex"

# Main page
MAIN_MENU = False
HOME_HIDE_TAGS = True
DISPLAY_PAGES_ON_MENU = True
PAGES_SORT_ATTRIBUTE = "order"

# Social

SOCIAL = (
    ('twitter', 'https://twitter.com/neiloxtoby'),
    ('github', 'https://github.com/noxtoby'),
    ('google','https://scholar.google.com/citations?user=uWfRPHEAAAAJ&hl=en'),
)


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

# Plugins
#PLUGIN_PATHS = ['plugins', 'plugins/pelican-embed-tweet']
#PLUGINS = ['render_math', 'embed_tweet']
#JINJA_ENVIRONMENT = {}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
