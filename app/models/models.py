# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base  # 创建模型继承的父类
from sqlalchemy.dialects.mysql import BIGINT, TEXT, DATETIME, VARCHAR, TINYINT  # 导入字段类型
from sqlalchemy import Column  # 定义字段
from werkzeug.security import check_password_hash  # 检查密码

# 创建父类
Base = declarative_base()
metadata = Base.metadata


# 创建消息保存模型
class Msg(Base):
    __tablename__ = "msg"  # 指定表名称
    id = Column(BIGINT, primary_key=True)  # 编号
    content = Column(TEXT)  # 内容
    createdAt = Column(DATETIME, nullable=False)  # 创建时间
    updatedAt = Column(DATETIME, nullable=False)  # 修改时间


# 创建会员模型
class User(Base):
    __tablename__ = "user"  # 指定表名称
    id = Column(BIGINT, primary_key=True)  # 编号
    name = Column(VARCHAR(20), nullable=False, unique=True)  # 昵称
    pwd = Column(VARCHAR(255), nullable=False)  # 密码
    email = Column(VARCHAR(100), nullable=False, unique=True)  # 邮箱
    phone = Column(VARCHAR(11), nullable=False, unique=True)  # 手机
    sex = Column(TINYINT, nullable=True)  # 性别
    xingzuo = Column(TINYINT, nullable=True)  # 星座
    face = Column(VARCHAR(100), nullable=True)  # 头像
    info = Column(VARCHAR(600), nullable=True)  # 介绍
    createdAt = Column(DATETIME, nullable=False)  # 创建时间
    updatedAt = Column(DATETIME, nullable=False)  # 修改时间

    # 验证密码
    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)


if __name__ == "__main__":
    import mysql.connector  # 导入数据库连接驱动
    from sqlalchemy import create_engine  # 创建连接引擎

    # 数据库连接配置
    mysql_configs = dict(
        db_host="192.168.0.101",
        db_name="mysql",
        db_port=3306,
        db_user="root",
        db_pwd="a1s2d3"
    )

    # 创建连接引擎，连接地址、编码、是否输出日志
    # 连接格式：'数据库系统名称+连接驱动名称://用户:密码@主机:端口/数据库名称'
    engine = create_engine(
        'mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'.format(
            **mysql_configs
        ),
        encoding="utf-8",
        echo=True
    )

    # 元类映射到数据库中去
    metadata.create_all(engine)
