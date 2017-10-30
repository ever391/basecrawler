# coding:utf8
from bs4 import BeautifulSoup
from selenium import webdriver
from basecrawler.basecrawler import BaseCrawler
import unittest

class TestPy3(unittest.TestCase):

    def setUp(self):
        self.bc = BaseCrawler()

    def test_get_phantomjs_browser(self):
        browser = self.bc.get_phantomjs_browser()
        self.assertIsInstance(browser, webdriver.PhantomJS)

    def test_basecrawler(self):
        source_url = 'http://tech.hqew.com/fangan/001002014'
        response = self.bc.requests_get(source_url)
        self.assertEqual(response.status_code, 200)
        response.encoding = 'utf8'
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        content_urls = self.bc.css_parser_urls(soup, 'div.tech-article-info h3 a')
        self.assertEqual(len(content_urls), 12)
        content_url = self.bc.get_full_url(source_url, content_urls[0])
        self.assertTrue('http' in content_url)

    def test_datetime_format(self):
        datetime = u'星期四, 十月 29, 2015'
        res = self.bc.datetime_format(datetime)
        self.assertEqual('2015-10-29', res)

    def test_get_proxy_ips(self):
        res = self.bc.get_proxy_ips()
        self.assertEqual(len(res) , 100)

if __name__ == "__main__":
    unittest.main()