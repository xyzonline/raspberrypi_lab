#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
import requests
import BaiduYuyin as pby #需要python2
import local
YOUR_APP_KEY = local.BAIDU_APP_KEY
YOUR_SECRET_KEY = local.BAIDU_SECRET_KEY
tts = pby.TTS(app_key=YOUR_APP_KEY, secret_key=YOUR_SECRET_KEY) # 默认带有秘钥
# 语音到文字
#user_input='你好啊'
#tts.say(user_input)
import pc_client
import json
import BaiduYuyin as pby

'''
ai模块
'''


r = pby.Recognizer()
def get_input():
  pc_client.say(u'请开始说话')
  with pby.Microphone() as source:
    audio = r.listen(source,timeout=0) #自动判断
    user_input = r.recognize(audio)
    print('user_input',user_input)
    return user_input


def get_response(query):
    turing_api = "http://www.tuling123.com/openapi/api"
    payload={}
    payload['key']=local.turing_key
    payload['info']=query
    response = requests.get(turing_api,params=payload)
    # 如果成功
    return response.json()

def turing_ai_talk():
    while True:
        info=get_input().encode('utf-8')
        response = get_response(info)
        response_text = response['text']
        pc_client.say(response_text)

turing_ai_talk()
# ai_talk()
# http://www.tuling123.com/

# pip show BaiduYuyin
# vim /Users/wwj/env/lib/python2.7/site-packages/BaiduYuyin/__init__.py
