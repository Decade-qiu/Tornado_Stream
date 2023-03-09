# -*- coding: utf-8 -*-
import tornado.gen
import tornado.concurrent
from app.views.views_common import CommonHandler
from app.tools.orm import ORM
from app.models.models import Stream


# 定义一个视图
class myStreamHandler(CommonHandler):
    # 定义一个GET请求的方法
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        data = dict(
            title="直播列表",
            stream=''
        )
        session = ORM.db()
        try:
            model = None
            model = session.query(Stream).filter_by(userid=self.name).order_by(Stream.createdAt.desc())
            if model != None: data['stream'] = self.page(model)
        except Exception as e:
            session.rollback()
            print(e)
        else:
            session.commit()
        finally:
            session.close()
        self.html("myStream.html", data=data)
