# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import random
import datetime

class WeiboPipeline(object):
    def __init__(self):
        self.host = "localhost"
        self.username = "root"
        self.pwssword = "123456"
    def process_item(self, item, spider):
        conn = pymysql.connect(self.host, self.username, self.pwssword)
        cursor = conn.cursor()
        topic_id = "topic" + self.createId()
        dicu_id = "dicu" + self.createId()
        sqlQuerytoTopic = "insert into weibo.t_weibo_topic values('%s', '%s', '%s', '%s', '%s')" % \
                          (topic_id, item['topic_content'], item['read_num'], item['dicu_num'], str(datetime.datetime.now()))
        sqlQuerytoDicu = "insert into weibo.t_weibo_dicu values('%s', '%s', '%s', '%s', '%s')" % \
                        (dicu_id, topic_id, item['dicu_content'], item['source'], item['release_time'])
        cursor.execute(sqlQuerytoTopic)
        cursor.execute(sqlQuerytoDicu)
        conn.commit()
        conn.close()
        return item

    def createId(self):
        chars = 'a0v1c2d3e4f5g6h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x4y5z6'
        salt = ''
        for i in range(10):
            salt += random.choice(chars)
        return salt
