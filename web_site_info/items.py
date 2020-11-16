# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebSiteInfoItem(scrapy.Item):
    logo = scrapy.Field()
    phones = scrapy.Field()
    website = scrapy.Field()
