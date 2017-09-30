快速说明
==========

简介
-------

BaseCrawler是一个轻量级，简单快捷上手操作基础爬虫框架，对于爬虫开发者，有很多实用的功能已经进行了优化与完善。
API说明文档请访问：http://www.basecrawler.com(目前暂时未上线)


安装说明
----------

    PIP 安装

    ``pip install basecrawler``

使用说明——方式一
-------------------

    首先我们引入BaseCrawler ::

        from basecrawler.basecrawler import BaseCrawler

    声明一个url地址， 例如: ::

        url = http://www.baidu.com

    实例化一个BaseCrawler对象 ::

        basecrawler = BaseCrawler()

    通过basecrawler请求目标url ::

        response = basecrawler.static_downloader_get(url)

    ``response`` 是requests.Response对象，输出返回的结果内容 ::

        print response.text

使用说明——方式二
------------------

如果我们采用面创建类的方式实现，可以直接继承 ``BaseCrawler`` ::

    from basecrawler.basecrawler import BaseCrawler

    class Crawler(BaseCrawler):

        # 定义你自己的类方法
        def foo():
            pass

    if __name__ == "__main__":
        crawler = Crawler()
        url = http://www.baidu.com
        crawler.static_downloader_get(url)


支持反反爬
----------

    目前完成基础反反爬处理, 根据反反爬策略可以选择不同的处理方式

支持动态网页爬取
---------------

    支持处理JS加载数据处理, 同时完成对 Phantomjs 性能优化

支持代理
---------

    支持 ``requests`` 及 ``phantomjs`` 代理

支持翻页处理
------------

    * 实现web网站翻页处理, 按API格式设置，可自动完成翻页处理

支持自动获取免费代理
-------------------

    * basecrawler内含获取代理IP方法，单次调用提供99个免费IP, 因验证ip会加大代理负载，IP不做验证处理，即时即用




