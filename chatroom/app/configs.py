# -*coding:utf-8
import os

# 获取当前文件所在的目录
from app.ui.ui_page import PageUI

root_path = os.path.dirname(__file__)

configs = dict(
    debug=True,  # 调试模式，如果为开发模式：True,如果为生成模式：False
    template_path=os.path.join(root_path, "templates"),  # 拼接当前路径和模板目录
    static_path=os.path.join(root_path, "static"),  # 拼接当前路径和静态文件目录
    xsrf_cookies=True,  # 开启xsrf保护，防止跨域请求
    cookie_secret='1c0a6ffe-14c3-4ac4-a974-3bb02a9a8b17',  # 密钥
    ui_modules=dict(
        page=PageUI
    )
)

# 主机、端口、名称、用户、密码
mysql_configs = dict(
    db_host="127.0.0.1",
    db_port=3306,
    db_name="chatroom_project",
    db_user="root",
    db_pwd="123456"
)

# redis主机、端口、库
redis_configs = dict(
    host="localhost",
    port=6379,
    db=0
)
