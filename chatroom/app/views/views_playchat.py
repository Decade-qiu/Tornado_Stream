# -*- coding: utf-8 -*-
import tornado.gen
import tornado.concurrent
from app.views.views_common import CommonHandler
from app.models.crud import CRUD


class PlayChatHandler(CommonHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        id = self.get_argument("id", None)
        if id:
            data = dict(
                title="弹幕视频"
            )
            data['video'] = CRUD.video(id)
            # print(data)
            self.html("playchat.html", data=data)
