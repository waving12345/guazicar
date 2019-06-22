# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class GuaziPipeline(object):

    def __init__(self, uri, database):
        self.uri = uri
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            uri=crawler.settings.get('MONGO_URI'),
            database=crawler.settings.get('MONGO_DB')
            )

    def open_spider(self, spider):
        # 获取数据库连接
        self.client = pymongo.MongoClient(self.uri)
        self.db = self.client[self.database]

    def close_spider(self, spider):
        # 释放数据库连接
        self.client.close()

    def process_item(self, item, spider):
        # 插入item数据
        collection_name = item.collection
        self.db[collection_name].insert(dict(item))
        return item