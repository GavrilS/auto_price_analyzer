# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from itemadapter import ItemAdapter
import psycopg2

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_USER = os.getenv('DB_USER', None)
DB_PASS = os.getenv('DB_PASS', None)
DB_NAME = os.getenv('DB_NAME', None)

# class CrawlerPipeline:
#     def process_item(self, item, spider):
#         return item


class OfferPipeline:
    def open_spider(self, spider):
        try:
            self.conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS,
                port=DB_PORT
            )
            self.cur = self.conn.cursor()
            print('DB connection set up successfully!')
        except Exception as e:
            print('Could not set up connection to the DB: ', str(e))


    def close_spider(self, spider):
        try:
            self.cur.close()
            self.conn.close()
            print('The connection to the DB was closed successfully!')
        except Exception as e:
            print('Could not close the connection to the database: ', str(e))

    
    def process_item(self, item, spider):
        user_id = item.get('user_id', 0)
        title = item.get('title', '')
        get_offer_query = f"SELECT * FROM offer WHERE user_id = {user_id} and title = {title}"
        result = self.cur.execute(get_offer_query).fetchone()
        if not result:
            pass
        else:
            pass
