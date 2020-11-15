import re
import scrapy

from web_site_info.items import WebSiteInfoItem, WebSiteInfoItemLoader

IMG_LOGO_XPATH = '//img[contains(@src, "logo")]/@src'
CONTACT_XPATH = '//a[contains(@href, "contact")]/@href'

class SiteInfoSpider(scrapy.Spider):
    name = 'site_info'
    start_urls = ['https://www.phosagro.com/']

    def parse(self, response):
        page_contact = response.xpath(CONTACT_XPATH).extract_first()
        yield response.follow(page_contact, self.parse_site_info)

    def parse_site_info(self, response):
        path_logo = self.extract_logo_path(response)
        phones = self.extract_phones(response)

        site_info = WebSiteInfoItemLoader(item=WebSiteInfoItem(), response=response)
        site_info.add_value('logo', path_logo)
        site_info.add_value('phones', phones)
        return site_info.load_item()

    def extract_logo_path(self, response):
        logo_path = response.urljoin(response.xpath(IMG_LOGO_XPATH).extract_first())
        return logo_path

    def extract_phones(self, response):
        page_text = response.xpath('normalize-space(//body)').extract_first()
        phones_pattern = r'[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*'
        phones = list(set(re.findall(phones_pattern, page_text)))
        return phones
