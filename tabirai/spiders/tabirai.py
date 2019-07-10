# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class TabiraiSpider(CrawlSpider):
    name = 'tabirai'
    allowed_domains = ['tabirai.net']
    start_urls = ['http://www.tabirai.net/hotel/sitemap/']

    rules = (
             Rule(LinkExtractor(restrict_xpaths=("//a[contains(@href, 'result.aspx')]",)), callback='parse_page',
                  follow=True),
             )

    def parse_page(self, response):
        yield from self.parse(response)  # make sure to rerun the rules for the second level

        if 'page' in response.url:  # make sure to only crawl paginated pages
            hotels = response.xpath("//*[@class='htl-card']")
            prefecture = response.url.split('hotel/')[1].split('/search')[0]

            self.crawler.stats.inc_value('counts/{}'.format(prefecture), len(hotels))
