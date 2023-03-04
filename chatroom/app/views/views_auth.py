# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler


# 登录权限的控制器
class AuthHandler(CommonHandler):
    # 在请求之前的预处理
    def prepare(self):
        # 如果name不存在，直接跳转到登录页面！
        if not self.name:
            print("illegal")
            self.redirect("/login/")
