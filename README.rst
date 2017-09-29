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






反爬
------

    目前完成基础反爬处理.

动态网页
-------

    支持处理JS加载数据处理

代理
------

    支持``requests`` 及 ``phantomjs`` 代理

翻页
------

    实现web网站翻页处理

自动更换免费代理
-----------------

    目前未加入此功能，后期会完成免费ip池处理

注意事项
----------

    **需要自行下载 ``imghdr`` 库**


