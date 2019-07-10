from scrapy.crawler import CrawlerProcess
from scrapy.conf import get_project_settings

from tabirai.spiders.tabirai import TabiraiSpider


if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())

    process.crawl(TabiraiSpider)
    process.start()
