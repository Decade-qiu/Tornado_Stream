# -*- coding: utf-8 -*-
import tornado.gen
import tornado.concurrent
from app.tools.forms import StreamBuildForm
from app.views.views_common import CommonHandler
from app.models.crud import CRUD


# 注册视图
class BuildHandler(CommonHandler):
    def check_xsrf_cookie(self):
        return True


    # 定义GET请求方法
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        data = dict(
            title="直播创建"
        )
        self.html("build.html", data=data)

    # 定义POST请求，专门处理注册表单
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        form = StreamBuildForm(self.fdata)
        print(form.data)
        res = dict(code=0)
        # 验证环节
        if form.validate():
            # 验证通过
            # print(form.data['url'])
            # 保存表单的数据到数据库user中去
            # if CRUD.save_regist_user(form):
            res["code"] = 1
        else:
            # 验证不通过
            res = form.errors
            res["code"] = 0
        self.write(res)  # 返回json接口信息
