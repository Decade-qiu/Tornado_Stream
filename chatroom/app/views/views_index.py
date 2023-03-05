# -*- coding: utf-8 -*-
import tornado.gen
import tornado.concurrent
from app.views.views_common import CommonHandler
from app.tools.orm import ORM
from app.models.models import Video


# 定义一个视图
class IndexHandler(CommonHandler):
    # 定义一个GET请求的方法
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        # self.write("<h1>这是一个弹幕视频+在线聊天的项目！</h1>")
        data = dict(
            title="视频列表"
        )
        session = ORM.db()
        q = self.get_argument("q", "")
        try:
            if q:
                model = session.query(Video).filter(
                    Video.name.like('%{}%'.format(q))
                ).order_by(Video.createdAt.desc())
            else:
                model = session.query(Video).order_by(Video.createdAt.desc())
            data['video'] = self.page(model)
            data['q'] = q
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        self.html("index.html", data=data)
