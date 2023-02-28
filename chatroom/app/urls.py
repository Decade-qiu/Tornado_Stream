# -*coding:utf-8

from app.views.views_index import IndexHandler as index  # 导入index视图

# 定义视图和路由的映射规则
urls = [
    (r"/", index)
]
