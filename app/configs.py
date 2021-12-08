# -*- coding: utf-8 -*-
import os  # 文件目录操作模块

# 常用配置
# 调试模式：开发者生产模式，debug=True
# 模板路径：template_path
# 静态文件路径：static_path
# 开启跨站伪装登录，xsrf_cookies=True
# 密钥，cookie_secret='xxxxxxxxxx'

# 获取当前文件所在目录
root_path = os.path.dirname(__file__)

# 站点配置
configs = dict(
    debug=True,
    template_path=os.path.join(root_path, "templates"),
    static_path=os.path.join(root_path, "static"),
    xsrf_cookies=True,
    cookie_secret='a1ca2e68bd364596a1c307f804466261'
)

# 数据库连接配置
mysql_configs = dict(
    db_host="localhost",
    db_name="mysql",
    db_port=3306,
    db_user="root",
    db_pwd="a1s2d3"
)
