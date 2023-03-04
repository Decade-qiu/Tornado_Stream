# -*- coding: utf-8 -*-
import tornado.gen
import tornado.concurrent
from app.views.views_auth import AuthHandler
from app.tools.forms import UserProfileEditForm
from app.models.crud import CRUD
from app.params import data as xz


# 个人资料视图
class UserProfileHandler(AuthHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        data = dict(
            title="个人资料",
            user=CRUD.user(self.name),
            xz=xz['xingzuo']
        )
        self.html("userprofile.html", data=data)

    # post方法
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        form = UserProfileEditForm(self.fdata)
        res = dict(code=0)
        if form.validate():
            # 保存用户信息
            if CRUD.save_user(form):
                res["code"] = 1
        else:
            res = form.errors
            res["code"] = 0
        self.write(res)
