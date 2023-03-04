# -*- coding: utf-8 -*-
import math
import tornado.web
from tornado.escape import utf8
from tornado.util import unicode_type
from werkzeug.datastructures import MultiDict
from app.models.crud import CRUD
from concurrent.futures import ThreadPoolExecutor


class CommonHandler(tornado.web.RequestHandler):
    # 定义线程池
    executor = ThreadPoolExecutor(1000)

    # 获取客户端提交过来的参数
    @property
    def params(self):
        # 获取参数方式，里面是一些二进制信息，字典类型
        data = self.request.arguments
        # 定义二进制转化utf-8编码
        # print(data)
        data = {
            k: list(
                map(
                    lambda val: str(val, encoding="utf-8"),
                    v
                )
            )
            for k, v in data.items()
        }
        # print(data)
        return data

    # 定义表单接受数据类型
    @property
    def fdata(self):
        # print(MultiDict(self.params))
        return MultiDict(self.params)

    # 定义获取账号名称
    @property
    def name(self):
        return self.get_secure_cookie("name", None)

    # 定义获取用户
    @property
    def user(self):
        if self.name:
            return CRUD.user(self.name)
        else:
            return None

    # 定义分页方法
    def page(self, model):
        # 获取页码
        page = self.get_argument("page", 1)
        page = int(page)
        # 统计数据表中有多少条记录
        total = model.count()
        if total:
            # 每页显示多少条
            shownum = 6
            # 确定总共显示多少页
            pagenum = int(math.ceil(total / shownum))
            # 判断小于第一页
            if page < 1:
                page = 1
            # 判断大于最后一页
            if page > pagenum:
                page = pagenum

            # sql限制查询，每次查询限制多少条，偏移量是多少
            offset = (page - 1) * shownum
            # 分页查询
            data = model.limit(shownum).offset(offset)
            # 上一页
            prev_page = page - 1
            next_page = page + 1
            if prev_page < 1:
                prev_page = 1
            if next_page > pagenum:
                next_page = pagenum
            arr = dict(
                pagenum=pagenum,
                page=page,
                prev_page=prev_page,
                next_page=next_page,
                data=data
            )
        else:
            arr = dict(
                data=[]
            )
        return arr

    def html(self, template_name, **kwargs):
        if self._finished:
            raise RuntimeError("Cannot render() after finish()")
        html = self.render_string(template_name, **kwargs)

        # Insert the additional JS and CSS added by the modules on the page
        js_embed = []
        js_files = []
        css_embed = []
        css_files = []
        html_heads = []
        html_bodies = []
        for module in getattr(self, "_active_modules", {}).values():
            embed_part = module.embedded_javascript()
            if embed_part:
                js_embed.append(utf8(embed_part))
            file_part = module.javascript_files()
            if file_part:
                if isinstance(file_part, (unicode_type, bytes)):
                    js_files.append(file_part)
                else:
                    js_files.extend(file_part)
            embed_part = module.embedded_css()
            if embed_part:
                css_embed.append(utf8(embed_part))
            file_part = module.css_files()
            if file_part:
                if isinstance(file_part, (unicode_type, bytes)):
                    css_files.append(file_part)
                else:
                    css_files.extend(file_part)
            head_part = module.html_head()
            if head_part:
                html_heads.append(utf8(head_part))
            body_part = module.html_body()
            if body_part:
                html_bodies.append(utf8(body_part))

        if js_files:
            # Maintain order of JavaScript files given by modules
            js = self.render_linked_js(js_files)
            sloc = html.rindex(b'</body>')
            html = html[:sloc] + utf8(js) + b'\n' + html[sloc:]
        if js_embed:
            js = self.render_embed_js(js_embed)
            sloc = html.rindex(b'</body>')
            html = html[:sloc] + js + b'\n' + html[sloc:]
        if css_files:
            css = self.render_linked_css(css_files)
            hloc = html.index(b'</head>')
            html = html[:hloc] + utf8(css) + b'\n' + html[hloc:]
        if css_embed:
            css = self.render_embed_css(css_embed)
            hloc = html.index(b'</head>')
            html = html[:hloc] + css + b'\n' + html[hloc:]
        if html_heads:
            hloc = html.index(b'</head>')
            html = html[:hloc] + b''.join(html_heads) + b'\n' + html[hloc:]
        if html_bodies:
            hloc = html.index(b'</body>')
            html = html[:hloc] + b''.join(html_bodies) + b'\n' + html[hloc:]
        return self.write(html)
