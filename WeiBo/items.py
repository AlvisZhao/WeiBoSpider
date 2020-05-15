# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topic_content = scrapy.Field()
    read_num = scrapy.Field()
    dicu_num = scrapy.Field()

    dicu_content = scrapy.Field()
    source = scrapy.Field()
    release_time = scrapy.Field()

    pass
