# -*coding:utf-8 -*
import sqlalchemy
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column  # 定义字段
from sqlalchemy.dialects.mysql import *  # 导入字段类型

# 1.创建模型继承的基类
Base = declarative_base()
metadata = Base.metadata


# 定义视频数据模型
class Video(Base):
    __tablename__ = "video"  # 定义数据表的名称
    id = Column(INTEGER, primary_key=True)  # 编号
    name = Column(VARCHAR(255), nullable=False)
    url = Column(VARCHAR(255), nullable=False)
    logo = Column(VARCHAR(255), nullable=False)
    createdAt = Column(DATETIME, nullable=False)  # 创建时间
    updatedAt = Column(DATETIME, nullable=False)  # 修改时间


# 定义聊天数据模型
class Msg(Base):
    __tablename__ = "msg"
    id = Column(BIGINT, primary_key=True)  # 编号
    content = Column(TEXT)  # 消息
    createdAt = Column(DATETIME, nullable=False)  # 创建时间
    updatedAt = Column(DATETIME, nullable=False)  # 修改时间


# 定义会员数据模型
class User(Base):
    __tablename__ = "user"
    id = Column(INTEGER, primary_key=True)  # 编号
    name = Column(VARCHAR(20), nullable=False, unique=True)  # 昵称
    pwd = Column(VARCHAR(255), nullable=False)  #
    email = Column(VARCHAR(100), nullable=False, unique=True)  #
    phone = Column(VARCHAR(11), nullable=False, unique=True)  #
    sex = Column(TINYINT, nullable=True)  # 性别
    xingzug = Column(TINYINT, nullable=True)  #
    face = Column(VARCHAR(100), nullable=True)  #
    info = Column(VARCHAR(600), nullable=True)  # 个性签名
    createdAt = Column(DATETIME, nullable=False)  # 创建时间
    updatedAt = Column(DATETIME, nullable=False)  # 修改时间


# 把models.py当作一个主执行文件运行
if __name__ == "__main__":
    import mysql.connector  # 数据库底层连接驱动
    from sqlalchemy import create_engine  # 创建连接引擎

    # 主机、端口、名称、用户、密码
    mysql_configs = dict(
        db_host="127.0.0.1",
        db_port=3306,
        db_name="chatroom_project",
        db_user="root",
        db_pwd="123456"
    )
    # 连接信息，数据库类型+数据库连接驱动：//用户：密码@主机：端口/数据库名称
    link = "mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}".format(
        **mysql_configs
    )
    # 创建连接引擎，encoding编码，echo是[True]否[False]输出日志
    engine = create_engine(
        link,
        connect_args={'charset': 'utf8'},
        echo=True
    )
    # 模型映射生成数据表
    metadata.create_all(engine)
