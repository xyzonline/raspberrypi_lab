#!/usr/bin/env python
# encoding: utf-8
#from __future__ import unicode_literals
# 百度语音模块
# 图灵api
import requests
import local

def get_response(query):
    turing_api = "http://www.tuling123.com/openapi/api"
    payload={}
    payload['key']=local.turing_key
    payload['info']=query
    response = requests.get(turing_api,params=payload)
    # 如果成功
    return response.json()['text']

