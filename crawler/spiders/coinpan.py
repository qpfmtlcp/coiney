# -*- coding: utf-8 -*-
import scrapy


class CoinpanSpider(scrapy.Spider):
    name = 'coinpan'
    allowed_domains = ['coinpan.com']
    start_urls = ['http://coinpan.com/']
    
    def parse(self, response):
        self.logger.info('I am here "%s"', response.url)
