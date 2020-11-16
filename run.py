from scrapyscript import Job, Processor
from scrapy.utils.project import get_project_settings


from web_site_info.spiders.site_info import SiteInfoSpider



if __name__ == "__main__":

    start_urls = ['https://www.phosagro.com/', 'https://www.cmsenergy.com/']
    jobs = list()

    for url in start_urls:
        job = Job(SiteInfoSpider, url=url)
        jobs.append(job)

    settings = get_project_settings()
    processor = Processor(settings)
    data = processor.run(jobs)

    for item in data:
        print(item['_values'])