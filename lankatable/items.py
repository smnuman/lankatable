# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LankatableItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ticker   = scrapy.Field()
    industry = scrapy.Field()
    yearEnd  = scrapy.Field()
    summery  = scrapy.Field()   # should hold 'summery' tsble from the page
    balance  = scrapy.Field()   # should hold 'Balance-sheet' tsble from the page
    income   = scrapy.Field()   # should hold 'income-statemnt' tsble from the page
    cash     = scrapy.Field()   # should hold 'cash-flow' tsble from the page
