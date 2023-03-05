# -*- coding: utf-8 -*-
import re
import numpy as np
import tornado.gen
import tornado.concurrent
from app.views.views_common import CommonHandler
from app.tools.orm import ORM
from app.models.models import Video

# 定义的全局变量
people_name = []  # 保存所有参与抽奖的人员
people_reward1_name = []  # 抽中一等奖的人员名单
people_reward2_name = []  # 抽中二等奖的人员名单
people_reward3_name = []  # 抽中三等奖的人员名单
falg = 0  # 每次只显示抽奖人数的一部分，不能全部显示出来,一等奖一名，二等奖两名，三等奖三名
people_reward1 = 0  # 一等奖中奖人数
people_reward2 = 0  # 二等奖中奖人数
people_reward3 = 0  # 三等奖中奖人数
flag1 = ""  # 一等奖是否一次性抽完,yes:一次性抽完；no：分批次抽完
flag2 = ""  # 二等奖是否一次性抽完,yes:一次性抽完；no：分批次抽完
flag3 = ""  # 三等奖是否一次性抽完,yes:一次性抽完；no：分批次抽完
pfull = ""
p1 = ""
p2 = ""
p3 = ""

def fun1(peoplestr):
    # 字符串处理函数，主要将文件内容（名字）存放到列表中
    pattern = r','
    result = re.split(pattern, peoplestr)
    return result

class InfoHandler(CommonHandler):
    def check_xsrf_cookie(self):
        return True
    
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        # self.write("<h1>这是一个弹幕视频+在线聊天的项目！</h1>")
        data = dict(
            title="抽奖"
        )
        num_1 = self.get_argument("num1")
        num_2 = self.get_argument("num2")
        num_3 = self.get_argument("num3")
        global people_reward1, people_reward2, people_reward3, pfull, p1, p2, p3
        people_reward2 = int(num_2)
        people_reward3 = int(num_3)
        num = int(num_1) + int(num_2) + int(num_3)  # 一共有多少人中奖
        print(num)
        file = self.request.files  # 文件信息提取
        print(file)
        print(type(file))  # <class 'dict'>
        for inputname in file:
            http_file = file[inputname]
            print(http_file)
            people = http_file[0]['body']
        #  people.decode('ascii')
        print(people)
        print(type(people))  # <class 'bytes'>
        people_str = people.decode(encoding='utf-8')
        pfull = people_str
        print("people1", people_str, type(people_str))  # <class 'str'>

        results = fun1(people_str)
        print(results)
        global people_name  # 保存所有参与抽奖的人员
        people_name = results

        hight = len(results) - 1
        print(hight)
        ary1 = set()
        #  根据中奖总人数将所有中奖人员一次性全部抽出，放在集合之中
        # （因为前提是所有中奖人员没有重复，所以抽一次和抽三次结果是一样的）
        while len(ary1) < num:
            a = np.random.random_integers(low=0, high=hight, size=1)
            ary1.add(a[0])
        #  ary = random.sample(range(0, hight), num)
        #  将集合转成列表
        ary = list(ary1)
        print(ary)
        people_1 = []  # 存放一等奖中奖名单
        people_3 = []  # 存放二等奖中奖名单
        people_2 = []  # 存放三等奖中奖名单
        for i in ary[0:int(num_1)]:
            people_1.append(results[i])
        for j in ary[int(num_1):int(num_1) + int(num_2)]:
            people_2.append(results[j])
        for k in ary[int(num_1) + int(num_2):int(num_1) + int(num_2) + int(num_3)]:
            people_3.append(results[k])
        p1 = ",".join(people_1)
        p2 = ",".join(people_2)
        p3 = ",".join(people_3)
        data["people1"] = p1
        data["people2"] = p2
        data["people3"] = p3
        data["people_in"] = pfull
        data["num1"] = num_1
        data["num2"] = num_2
        data["num3"] = num_3
        data["people_len"] = len(people_name)
        data['win_len'] = num
        self.html("info.html", data=data)
