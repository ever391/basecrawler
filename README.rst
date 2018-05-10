快速说明
==========

简介
-------

BaseCrawler是一个轻量级，简单快捷上手操作基础爬虫工具库，对于爬虫开发者，有很多实用的功能已经进行了优化与完善。
BaseCrawler帮你处理各种类型怪异的url拼接错误问题，以及各种不同格式的时间，有很多小功能帮你解决头疼的问题。
API说明文档请访问：http://www.basecrawler.com
具体使用请查看文档
QQ交流群:662500882


版本支持
----------
    * Python 2.7.x
    * Python 3.x
    * 如python3发现Bug，请与我联系！

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

        response = basecrawler.requests_get(url)

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
        crawler.requests_get(url)


支持反反爬
----------

    * 目前完成基础反反爬处理, 根据反反爬策略可以选择不同的处理方式
    * 常见反爬的东西，大家就不要再自己码代码了，这里我进行处理了！
    *

支持动态网页爬取
---------------

    * 支持处理JS加载数据处理, 同时完成对 Phantomjs 性能优化
    * 想必大家在使用selenium中的PhantomsJS 时一定非常消耗性能哦，这里我已经完成性能优化，让它飞起来！

支持代理
---------

    * 支持 ``requests`` 及 ``phantomjs`` 代理
    * requests的代理可能大部分小伙伴都会加（如果不会，我这里也有哦）
    * PhantomJS不会使用代理的快来用吧！这里都给你做好了！

支持翻页处理
------------

    * 实现web网站翻页处理, 按API格式设置，可自动完成翻页处理

支持自动获取免费代理
-------------------

    * basecrawler内含获取代理IP方法，单次调用提供100个免费IP, 因验证ip会加大代理负载，IP不做验证处理，即时即用

支持图片下载与替换
-------------------

    * 支持将目标图片下载到OSS服务中

支持自动修复iframe视频地址
-------------------------

    * HTML中存在iframe视频，不能正常播放的，已经完成处理。

支持解析微信公众号文章列表
-----------------------

    * 解析公众号文章列表已经完成，只要你能拿到请求结果！（方法我就不公开了）

支持解析微信公众号文章内容
-----------------------

    * 如果在爬微信公众号的文章，输入文章页面地址，自动把解析结果给你，不要再做重复工作了！

长期维护，同步更新
---------------------

 - 2018-5-10 更新微信文章页面数据采集规则
