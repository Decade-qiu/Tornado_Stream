# -*- coding: utf-8 -*-
import tornado.gen
import tornado.concurrent
from app.views.views_common import CommonHandler
from app.tools.forms import LoginForm


# 登录视图
class LoginHandler(CommonHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        data = dict(
            title="登录"
        )
        self.html("login.html", data=data)

    # post请求
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        form = LoginForm(self.fdata)
        res = dict(code=0)
        if form.validate():
            res["code"] = 1
            # 保存本地登录会话
            self.set_secure_cookie("name", form.data['name'])
        else:
            res = form.errors
            res["code"] = 0
        self.write(res)
