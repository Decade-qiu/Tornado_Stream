# -*- coding: utf-8 -*-
import tornado.gen
import tornado.concurrent
from app.views.views_common import CommonHandler
from app.tools.orm import ORM
from app.models.models import Video


# 定义一个视图
class LotteryHandler(CommonHandler):
    # 定义一个GET请求的方法
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        # self.write("<h1>这是一个弹幕视频+在线聊天的项目！</h1>")
        data = dict(
            title="抽奖配置"
        )
        self.html("lottery.html", data=data)
