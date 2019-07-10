# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TabiraiPipeline(object):
    def process_item(self, item, spider):
        item['coordinates'] = self.to_degrees(item['coordinates'][0]), self.to_degrees(item['coordinates'][1])
        return item

    @staticmethod
    def to_degrees(millis):
        return millis / 3600000
