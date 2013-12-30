#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tytouf'
SITENAME = u'Tytouf\'s Blog'
SITEURL = 'http://tytouf.github.com/blog'
RELATIVE_URLS = True

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = 'themes/subtle'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

# Blogroll
LINKS =  (('Makerspace56', 'http://makerspace56.org'),)

# Social widget
SOCIAL = (('github', 'http://github.com/tytouf'),
          ('twitter', 'http://twitter.com/tytouf'),
          ('linkedin', 'http://www.linkedin.com/pub/christophe-augier/1/562/660'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
