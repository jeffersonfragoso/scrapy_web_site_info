from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from web_site_info.spiders.site_info import SiteInfoSpider


process = CrawlerProcess(get_project_settings())
process.crawl(SiteInfoSpider)
process.start()