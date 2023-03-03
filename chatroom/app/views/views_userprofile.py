# -*coding:utf-8

import tornado.web


# 定义一个视图
class UserProfileHandler(tornado.web.RequestHandler):
    # 定义一个GET清求的方法
    def get(self, *args, **kwargs):
        data = dict(
            title="个人资料"
        )
        self.render("userprofile.html", data=data)
