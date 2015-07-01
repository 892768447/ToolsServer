#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年6月16日
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
import sys

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from application import WebApplication


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

def start():
    try:
        port = int(sys.argv[1].split("=")[1])
    except:
        port = 8000
    server = HTTPServer(WebApplication())
    server.listen(port)
    IOLoop.instance().start()

def stop():
    IOLoop.instance().stop()

if __name__ == "__main__":
    start()
