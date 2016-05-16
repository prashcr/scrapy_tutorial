# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, Join

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field(
        input_processor=MapCompose(
            lambda x: ' '.join(x.split()),
            lambda x: x.upper()
        ),
        output_processor=Join()
    )
