# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import re
import scrapy

from itemloaders.processors import MapCompose
from scrapy.loader import ItemLoader

class WebSiteInfoItem(scrapy.Item):
    logo = scrapy.Field()
    phones = scrapy.Field()
    website = scrapy.Field()


class WebSiteInfoItemLoader(ItemLoader):
    def sanitize_phone(phones):
        """
            Remove any characters that are not digits, a plus sign (+) or parentheses.

            Parameters:
                - phoness (list) - Object whit text phones extracted
        """

        pattern = r'[+()\s]|[0-9]'
        return ["".join(re.findall(pattern, phone)) for phone in phones]

    phones_in = MapCompose(sanitize_phone)
