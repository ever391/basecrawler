# coding:utf8
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from basecrawler.basecrawler import BaseCrawler, BeautifulSoup
import pymysql
from collections import OrderedDict
import re
import pymongo

class LianJia(BaseCrawler):

    def __init__(self):
        self.mysqldb = pymysql.connect("127.0.0.1", "root", "", "xiaoqu")
        self.cursor = self.mysqldb.cursor()
        self.mysqldb.charset = "utf8"
        self.cursor.execute("set names utf8")

        self.cursor.execute('set names utf8')
        self.cursor.execute('SET CHARACTER SET utf8mb4;')
        self.cursor.execute('SET character_set_connection=utf8;')

        self.mongo = pymongo.MongoClient(['127.0.0.1:27017'], maxPoolSize=10)
        self.mongodb = self.mongo["wechat"]

        super(LianJia, self).__init__()

    def run(self):
        page = 1
        while 1:
            url = "https://bj.lianjia.com/xiaoqu/pg%s/" % page
            print page
            self.get_content_urls(url)
            page += 1
            if page == 400:
                break


    def get_content_urls(self, url):
        try:
            resp = self.requests_get(url)
        except Exception as e:
            self.logger.error("req failure: ", str(e))
            return

        soup = BeautifulSoup(resp.text, 'lxml')
        for node_a in soup.select('div.info div.title a'):
            try:
                content_url = node_a["href"]
            except Exception as e:
                print str(e)
                continue
            print content_url

            data = self.get_content(content_url)
            if not data:
                data = OrderedDict()
            data["list_url"] = url
            data["content_url"] = content_url

            self.insert_data(data)

    def get_content(self, url):
        try:
            resp = self.requests_get(url)
        except Exception as e:
            self.logger.error("req content page failure: ", str(e))
            return

        soup = BeautifulSoup(resp.text, 'lxml')
        data = OrderedDict()
        try:
            data["name"] = soup.select("h1.detailTitle")[0].get_text().strip()
        except Exception as e:
            self.logger.error("get name field failure: ", str(e))
        try:
            data["address"] = soup.select(("div.detailDesc"))[0].get_text().strip()
        except Exception as e:
            self.logger.error("get address field failure: ", str(e))
        try:
            data["price"] = soup.select("span.xiaoquUnitPrice")[0].get_text().strip()
        except Exception as e:
            self.logger.error("get price field failure: ", str(e))
        try:
            create_year = soup.select("div.xiaoquInfo > div:nth-of-type(1) > span.xiaoquInfoContent")[0].get_text().strip()
            data["create_year"] = self.get_number(create_year)
        except Exception as e:
            self.logger.error("get create_year field failure: ", str(e))
        try:
            data["developer"] = soup.select("div.xiaoquInfo > div:nth-of-type(5) > span.xiaoquInfoContent")[0].get_text().strip()
        except Exception as e:
            self.logger.error("get developer field failure: ", str(e))
        try:
            buildings = soup.select("div.xiaoquInfo > div:nth-of-type(6) > span.xiaoquInfoContent")[0].get_text().strip()
            data["buildings"] = self.get_number(buildings)
        except Exception as e:
            self.logger.error("get buildings field failure: ", str(e))
        try:
            total = soup.select("div.xiaoquInfo > div:nth-of-type(7) > span.xiaoquInfoContent")[0].get_text().strip()
            data["total"] = self.get_number(total)
        except Exception as e:
            self.logger.error("get total field failure: ", str(e))
        try:
            data["province"] = soup.select("div.fl.l-txt a:nth-of-type(2)")[0].get_text().strip()
        except Exception as e:
            self.logger.error("get province field failure: ", str(e))
        try:
            data["city"] = soup.select("div.fl.l-txt a:nth-of-type(3)")[0].get_text().strip()
        except Exception as e:
            self.logger.error("get city field failure: ", str(e))
        return data

    def get_number(self, str):
        res = re.search(r'\d+', str, flags=re.S).group()
        return res

    def insert_data(self, data):
        try:
            self.mongodb["xiaoqu"].insert(data)
        except Exception as e:
            self.logger.error("mongo insert failure: ", str(e))

        sql = u'''insert into xiaoqu(id, province, city, `name`, total, price, create_year, developer, buildings, list_url, content_url, address)
VALUES (null, "{province}", "{city}", "{name}", {total}, {price}, {create_year}, "{developer}", {buildings}, "{list_url}", "{content_url}", "{address}")'''.format(
            province=data.get("province", u"北京"),
            city=data.get("city", u""),
            name=data.get("name", u""),
            total=data.get("total", 0),
            price=data.get("price", 0),
            create_year=data.get("create_year", 0),
            developer=data.get("developer", u""),
            buildings=data.get("buildings", 0),
            list_url=data.get("list_url", u""),
            content_url=data.get("content_url", u""),
            address=data.get("address", u""),
        )
        self.cursor.execute(sql.encode("utf8"))
        self.mysqldb.commit()


if __name__ == "__main__":
    lj = LianJia()
    lj.run()