import scrapy


class SiteInfoSpider(scrapy.Spider):
    name = 'site_info'
    allowed_domains = ['']
    start_urls = ['http:///']

    def parse(self, response):
        pass
