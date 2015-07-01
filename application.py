#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年6月16日
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
import base64
import uuid

from tornado.web import Application

from handler import IndexHandler, TestHandler


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

class WebApplication(Application):

    def __init__(self):
        settings = {
            "cookie_secret": base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
            "xsrf_cookies": False,
            "autoescape": None,
            "gzip": True,
            "static_path": "static",
            "debug": False,
        }
        Application.__init__(self, [(r"/test", TestHandler), (r"/(.*)", IndexHandler)], **settings)