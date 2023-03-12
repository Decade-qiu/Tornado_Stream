# -*- coding: utf-8 -*-
import tornado.gen
import tornado.concurrent
from app.views.views_common import CommonHandler
from app.tools.orm import ORM
from app.models.models import Video


# 定义一个视图
class StreamHandler(CommonHandler):
    def check_xsrf_cookie(self):
        return True
    # 定义一个GET请求的方法
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        data = dict(
            title="Stream"
        )
        app = self.get_argument('app', '')
        name = self.get_argument('name', '')
        if app != '' and name != '':
            data['app'] = app
            data['name'] = name
        # data["http_url"] = "http://127.0.0.1:80/live?port=1935&app=myapp&stream=STREAM_NAME"
        self.html("stream.html", data=data)
    
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        rtmp_url = self.get_argument('url', "")+"/t/t/t/t"
        rtmp, myapp, name = rtmp_url[7:].split('/')[0:3]
        res = dict(
            app=myapp,
            name=name
        )
        self.write(res)
        # data["http_url"]="http://{}:{}/live?port={}%26app={}%26stream={}".format(
        #         "127.0.0.1",
        #         "80",
        #         "1935",
        #         app,
        #         name