#!/usr/bin/env python
# encoding: utf-8
#from __future__ import unicode_literals
# 图灵api
import requests
import settings

def get_response(query):
    '''
    与云端ai交互
    '''
    turing_api = "http://www.tuling123.com/openapi/api"
    payload={}
    payload['key']=settings.turing_key
    payload['info']=query
    response = requests.get(turing_api,params=payload)
    # todo: 判断网络请求是否成功，设置超时
    return response.json()['text']

