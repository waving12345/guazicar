# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from guazi.items import GuaziItem


class CarSpider(scrapy.Spider):
    name = 'car'

    def start_requests(self):

        for page in range(1, 51):
            href = 'https://www.guazi.com/cd/buy/o{}/#bread'.format(page)
            yield Request(href, callback=self.parse_car, dont_filter=True)


    def parse_car(self, response):
        # print(response.text)
        products = response.xpath('//html/body/div[6]/ul/li')
        for pruduct in products:
            item = GuaziItem()
            item['name'] = pruduct.xpath('./a/h2/text()').extract_first()
            item['price'] = pruduct.xpath('./a/div[2]/p/text()').extract_first() + '万'
            item['date'] = pruduct.xpath('./a/div[1]/text()[1]').extract_first()
            item['trip'] = pruduct.xpath('./a/div[1]/text()[2]').extract_first()
            item['service'] = pruduct.xpath('./a/div[1]/text()[3]').extract_first()
            item['tags'] = pruduct.xpath('./a/div[2]/i/text()').extract()
            item['pic'] = pruduct.xpath('./a/img/@src').extract_first()

            # print(item['name'], item['price'], item['date'], item['trip'], item['service'], item['tags'], item['pic'])
            yield item
