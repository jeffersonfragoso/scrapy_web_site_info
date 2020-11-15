import scrapy
from web_site_info.items import WebSiteInfoItem, WebSiteInfoItemLoader

IMG_LOGO_XPATH = '//img[contains(@src, "logo")]/@src'

class SiteInfoSpider(scrapy.Spider):
    name = 'site_info'
    start_urls = ['https://www.phosagro.com/']

    def parse(self, response):
        site_info = WebSiteInfoItemLoader(item=WebSiteInfoItem(), response=response)
        path_image = response.urljoin(response.xpath(IMG_LOGO_XPATH).extract_first())

        site_info.add_value('logo', path_image)
        return site_info.load_item()
