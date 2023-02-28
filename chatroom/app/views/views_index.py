# -*coding:utf-8

import tornado.web


# 定义一个视图
class IndexHandler(tornado.web.RequestHandler):
    # 定义一个GET清求的方法
    def get(self, *args, **kwargs):
        self.write("<h1>这是一个弹幕视频+在线聊天的项目！</h1>")
