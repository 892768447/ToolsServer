#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年6月17日
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
from urllib.parse import urlencode

from tornado import gen
from tornado.httpclient import HTTPRequest
from tornado.ioloop import IOLoop


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://user.qzone.qq.com/892768447"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

# ━━━━━━神兽出没━━━━━━
# 　　 ┏ ┓　　　┏ ┓
# 　┏  ┛  ┻ ━ ━ ━  ┛ ┻  ┓
# 　┃　　　　　　　┃
# 　┃　　　 ━　　　 ┃
# 　┃　　┳┛　┗┳　　┃
# 　┃　　　　 　　　┃
# 　┃　 　　┻　　　 ┃
# 　┃　　　　　　　┃
# 　┗━┓　　　　　┏━┛
# 　　┃　　　　　┃神兽保佑
# 　　┃　　　　　┃代码无BUG！
# 　　┃　　　　　┗━━━┓
# 　　┃　　　　　　　 ┣┓
# 　　┃　　　　　　　 ┏┛
# 　　┗   ┓ ┓┏  ━  ━  ┳ ┓┏┛
# 　　　 ┃ ┫ ┫　　  ┃ ┫┫
# 　　　┗ ┻ ┛　　  ┗ ┻ ┛
# ━━━━━━感觉萌萌哒━━━━━━

try:
    from tornado.curl_httpclient import CurlAsyncHTTPClient as HttpClient    # @UnusedImport
except:
    from tornado.httpclient import AsyncHTTPClient as HttpClient    # @Reimport

client = HttpClient()

url = "http://www.baidu.com/s?"
method = "GET"
body = urlencode({"wd":"python"})


@gen.coroutine
def test():
    request = HTTPRequest(url = url + body, method = method)    # , body = body)
    result = yield gen.Task(client.fetch, request)
    print(result.body)
    print(type(result.headers), result.headers)
    print(result.headers.get("Bdpagetype"))
    # open("body.html", "wb").write(result.body)

test()
IOLoop.instance().start()
