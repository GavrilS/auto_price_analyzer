# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CarOffer(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    details = scrapy.Field()
    user_id = scrapy.Field()
    record_time = scrapy.Field()
