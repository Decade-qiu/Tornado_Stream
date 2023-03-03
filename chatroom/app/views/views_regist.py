# -*coding:utf-8

import tornado.web


# 定义一个视图
class RegistHandler(tornado.web.RequestHandler):
    # 定义一个GET清求的方法
    def get(self, *args, **kwargs):
        data = dict(
            title="注册"
        )
        self.render("regist.html", data=data)

