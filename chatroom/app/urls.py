# -*coding:utf-8
from app.views.views_index import IndexHandler as index  # 导入视频列表视图
from app.views.views_playchat import PlayChatHandler as playchat  # 导入弹幕视频视图
from app.views.views_regist import RegistHandler as regist  # 导入注册视图
from app.views.views_login import LoginHandler as login  # 导入登录视图
from app.views.views_userprofile import UserProfileHandler as userprofile  # 导入个人资料
from app.views.views_logout import LogoutHandler as logout  # 导入退出视图
from app.views.views_upload import UploadHandler as upload  # 导入上传视图
from app.views.views_dm import DMHandler as dm  # 弹幕接口
from app.views.views_chatroom import ChatRoomHandler as chatroom  # 聊天室ws接口
from app.views.views_msg import MsgHandler as msg  # 聊天接口
from sockjs.tornado import SockJSRouter
from app.views.views_main import MainHandler as main
from app.views.views_lottery import LotteryHandler as lottery
from app.views.views_info import InfoHandler as info
# from app.views.views_test import TestHandler as test

# 定义视图和路由的映射规则
urls = [
    (r"/", main),
    (r"/lottery/", lottery),
    (r"/info/", info),
    (r"/index/", index),
    (r"/playchat/", playchat),
    (r"/regist/", regist),
    (r"/login/", login),
    (r"/userprofile/", userprofile),
    (r"/logout/", logout),
    (r"/upload/", upload),
    (r"/msg/", msg),
    (r"/dm/v3/", dm),
] + SockJSRouter(chatroom, "/chatroom").urls
