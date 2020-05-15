# -*- coding: utf-8 -*-
import scrapy
from ..items import WeiboItem


class WeibospiderSpider(scrapy.Spider):
    name = "WeiBoSpider"
    start_urls = ['https://s.weibo.com/top/summary/']

    def parse(self, response):
        urls = response.xpath("//td[@class='td-02']/a/@href").getall()
        for url in urls:
            url = "https://s.weibo.com/" + url
            # print(url)
            yield scrapy.Request(url,callback=self.parse_detail)

    def parse_detail(self,response):
        topic_content = response.xpath("//h1/a/text()").extract()
        print(topic_content)

        item = WeiboItem
        yield item
