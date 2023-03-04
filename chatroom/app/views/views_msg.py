# -*- coding: utf-8 -*-
import json
import tornado.gen
import tornado.concurrent
from app.views.views_common import CommonHandler
from app.models.crud import CRUD


# 获取消息接口
class MsgHandler(CommonHandler):
    def check_xsrf_cookie(self):
        return True

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        data = CRUD.new_msg()
        result = []
        for v in data:
            result.append(json.loads(v.content))  # 转化为字典追加
        self.write(
            dict(
                data=result
            )
        )
