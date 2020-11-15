# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader

class WebSiteInfoItem(scrapy.Item):
    logo = scrapy.Field()
    phone = scrapy.Field()
    website = scrapy.Field()


class WebSiteInfoItemLoader(ItemLoader):

    default_input_processor = TakeFirst()
    default_output_processor = TakeFirst()
