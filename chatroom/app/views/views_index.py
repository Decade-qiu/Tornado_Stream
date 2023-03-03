# -*coding:utf-8

import tornado.web


# 定义一个视图
class IndexHandler(tornado.web.RequestHandler):
    # 定义一个GET清求的方法
    def get(self, *args, **kwargs):
        # self.write("<h1>项目！</h1>")
        data = dict(
            title="decade"
        )
        self.render("index.html", data=data)
