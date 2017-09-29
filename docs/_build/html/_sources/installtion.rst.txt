
安装说明
========

PIP 安装
----------

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

