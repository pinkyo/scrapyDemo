# -*- coding: utf-8 -*-
import scrapy

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        yield {
            "title": response.css("title::text").extract_first(),
            "url": response.url
        }

        for href in response.css('a::attr(href)'):
            url = href.extract()
            if url.startswith('http://'):
                yield scrapy.Request(url, callback=self.parse)
        pass
