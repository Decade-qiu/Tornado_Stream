# -*coding:utf-8
import os

# 获取当前文件所在的目录
root_path = os.path.dirname(__file__)

configs = dict(
    debug=True,  # 调试模式，如果为开发模式：True,如果为生成模式：False
    template_path=os.path.join(root_path, "templates"),  # 拼接当前路径和模板目录
    static_path=os.path.join(root_path, "static"),  # 拼接当前路径和静态文件目录
)

# 主机、端口、名称、用户、密码
mysql_configs = dict(
    db_host="127.0.0.1",
    db_port=3306,
    db_name="chatroom_project",
    db_user="root",
    db_pwd="123456"
)
