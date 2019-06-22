# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    collection = table = 'second-hand cars' # 集合
    name = scrapy.Field()  # 名称
    price = scrapy.Field()  # 价格
    date = scrapy.Field()  # 日期
    trip = scrapy.Field()  # 里程
    service = scrapy.Field()  # 服务
    tags = scrapy.Field()  # 标签
    pic = scrapy.Field()  # 图片



