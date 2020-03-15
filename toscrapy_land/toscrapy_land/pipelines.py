# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time
import re
import string
import MySQLdb

class ToscrapyLandPipeline(object):
    def process_item(self, item, spider):
        tdt = time.time()
        age = item.get('age')
        if age == 'Yesterday':
            fbt = tdt - 24 * 60 * 60
            item['age'] = time.strftime('%d/%m/%Y', time.gmtime(fbt))
        if age.find('hour')>=0:
            fbts = re.findall('\d+',age)
            fbt = tdt - string.atoi(fbts[0]) * 60 * 60 
            item['age'] = time.strftime('%d/%m/%Y', time.gmtime(fbt))
        if age.find('minute')>=0:
            fbts = re.findall('\d+',age)
            fbt = tdt - string.atoi(fbts[0]) * 60 
            item['age'] = time.strftime('%d/%m/%Y', time.gmtime(fbt))
        return item
        
class MySQLPipeline(object):
    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME', 'testdb')
        host = spider.settings.get('MYSQL_HOST', '47.105.187.15')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD','')
        self.db_conn = MySQLdb.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()
        
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()
        
    def process_item(self, item, spider):
        self.insert_db(item)
        return item
        
    def insert_db(self, item):
        values = (
            item['id'],
            item['title'],
            item['price'],
            item['negotiable'],
            item['age'],
            item['region'],
            item['location'],
        )
        sql = 'INSERT INTO lands VALUES (%s,%s,%s,%s,%s,%s,%s)'
        self.db_cur.execute(sql, values)
