# -*- coding: utf-8 -*-
# import pymongo
# from douban.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection
import MySQLdb
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def __init__(self):
        self.conn= MySQLdb.Connect(
                          host = '127.0.0.1',
                          port= 3306,
                          user='root',
                          passwd = 'root',
                          db = 'test',
                          charset = 'utf8'
                      )
    def process_item(self, item, spider):
        cursor = self.conn.cursor()
        sql_insert = "insert into movie(describe1,evaluate,introduce,movie_name,serial_number,star) values('"+ MySQLdb.escape_string(item['describe']) + "' ,'"+ item['evaluate'] + "','"+ item['introduce'] + "','"+ item['movie_name'] + "','"+ item['serial_number'] + "','"+ item['star'] + "')"
        cursor.execute(sql_insert)
        return item
