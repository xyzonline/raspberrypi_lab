#!/usr/bin/env python
# encoding: utf-8

'''
配置文件

# todo
从本地local.py导入隐私参数

# 设置开关（feature）
'''


#------------------<flask app settings>
APP_KEY = "test" # http请求需要携带的密码
CODE_FILE = './codetest.py' # 树莓派是用户的，假设其代码可信
#------------------<网络服务>  注意key的安全
# for 百度语音
access_token = "xxx"

# baidu app key and secret，用于请求生成access_token
YOUR_APP_KEY = "xxx"
YOUR_SECRET_KEY = "xx"

# turing bot
turing_key = 'xxx'

# email 用于报警模块
mail_host="smtp.qq.com"  #设置服务器
mail_user="pi@qq.com"    #用户名
mail_pass="xxx"   #密码

#------------------</网络服务>


#------------------<机器状态>
ONLINE = False # 默认单机转态
