# coding:utf8
from basecrawler.basecrawler import BaseCrawler
import re

class Wechat(BaseCrawler):

    def __init__(self):

        super(Wechat, self).__init__()


    def run(self):
        # 目标公众号列表页url
        url = "https://mp.weixin.qq.com/profile?src=3&timestamp=1524017195&ver=1&signature=bSSQMK1LY77M4O22qTi37cbhjhwNV7C9V4aor9HLhAsRpvNYY06GRNcVSPu0ovYiRAhQ*qvXrxgsV2Djm*re0Q=="
        # 返回的请求数据
        resp = self.requests_get(url)
        # 解析列表页面url
        urls = self.get_wechat_content_urls(resp.text)
        for url in urls:
            # 循环请求内容页面地址
            resp2 = self.requests_get(url)
            # 返回数据字段，标题， 简介， 内容， 时间，公众号名称
            data = self.get_wechat_content(resp2.text)
            print data





if __name__ == "__main__":
    wc = Wechat()
    wc.run()
