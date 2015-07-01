#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年6月16日
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''

import base64
import hashlib
import json
from urllib.parse import urlencode

from tornado import web, gen
from tornado.httpclient import HTTPRequest
from tornado.log import app_log
from tornado.web import RequestHandler


try:
    from tornado.curl_httpclient import CurlAsyncHTTPClient as HttpClient    # @UnusedImport
except:
    from tornado.httpclient import AsyncHTTPClient as HttpClient    # @Reimport @UnusedImport


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

def decrypt(data):
    '''
    # 解密算法
    '''
    pass

def encrypt(data):
    '''
    # 返回数据加密算法
    '''
    return base64.b64encode(str(data).encode()).decode()

class BaseHandler(RequestHandler):

    def finish(self, chunk = None):
        self.set_header("Server", "Tools Web Server")
        # self.set_header("Content-Type", "application/text/plain; charset=utf-8")
        super(BaseHandler, self).finish(chunk)

class TestHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.finish('''<html>
    <head>
        <title>测试</title>
    </head>
    <body>
        <center>
            <form action="/test" method="post" >
                <input type="text" name="test" value="" />
                <input type="submit" value="提交" />
            </form>
        </center>
    </body>
</html>''')

    def post(self, *args, **kwargs):
        test = self.get_argument("test")
        self.finish(test)

class IndexHandler(BaseHandler):

    @property
    def error(self):
        return encrypt(dict(code = 0, message = "操作失败"))

    def get(self, *args, **kwargs):
        self.finish("hello")

    @web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        try:
            ok, data = decrypt(self.get_argument("data"))
            if not ok:
                self.finish(self.error)
                return
            data = json.loads(data)
            url = data.get("url", "")
            print("url: ", url)
            method = data.get("method", "GET")
            print("method: ", method)
            headers = data.get("headers", {})
            print("headers: ", headers)
            body = data.get("body", {})
            print("body: ", urlencode(body))
            if not url or not data:
                self.finish(self.error)
                return
            if method == "GET":
                if not url.endswith("?"):
                    url = url + "?"
                url = url + urlencode(body)
                request = HTTPRequest(url = url, method = method, headers = headers)
            elif method == "POST":
                request = HTTPRequest(url = url, method = method, \
                headers = headers, body = urlencode(body))
            else:
                self.finish(self.error)
                return
            client = HttpClient()
            result = yield gen.Task(client.fetch, request)
            self.finish(encrypt(dict(code = result.code, message = "", \
                time = result.request_time, headers = result.headers, body = result.body.decode())))
        except Exception as err:
            self.finish(self.error)
            app_log.error(err, exc_info = 1)
