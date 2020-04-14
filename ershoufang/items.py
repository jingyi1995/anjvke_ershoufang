# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ErshoufangItem(scrapy.Item):
    # define the fields for your item here like:
    houseLoc = scrapy.Field()
    # houseEncode = scrapy.Field()
    houseInfo = scrapy.Field()
    propertyCosts = scrapy.Field()
    Community = scrapy.Field()
    totalPrice = scrapy.Field()
    houseHistoryPrice = scrapy.Field()
    # url = scrapy.Field()
    pass