# -*- coding: utf-8 -*-
from app.views.views_auth import AuthHandler


# 退出
class LogoutHandler(AuthHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie("name")
        self.redirect("/login/")
