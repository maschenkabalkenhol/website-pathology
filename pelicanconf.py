#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'WebteamDIAG'
SITENAME = u'Computational Pathology Group'
SITENAME_SHORT = 'CPG'
SITEURL = ''

PATH = 'content'
RELATIVE_URLS = False

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
#THEME = 'pathology-theme'
DEFAULT_PAGINATION = 10

# URL settings
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

ARTICLE_URL = 'news/{slug}/'
ARTICLE_SAVE_AS = 'news/{slug}/index.html'

CATEGORY_URL = 'categories/{slug}'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'

ARCHIVES_SAVE_AS = 'archives/index.html'

INDEX_SAVE_AS = 'news/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme settings
#
THEME="themes/pathology-theme"

# Plugins
#
PLUGIN_PATHS = ["plugins"] #Lib/site-packages
PLUGINS = ["edit_url", "hierarchy"]

# Other
EDIT_CONTENT_URL = 'https://github.com/diagnijmegen/website-pathology/edit/master/{file_path}'
