#!/usr/bin/env python
# encoding: utf-8
'''
# chatbot client
chatterbot作为本地服务，该模块是client
'''

import requests


localhost = "127.0.0.1"
local_server_base_url = 'http://{}:5001'.format(localhost)

def request_post(url,payload):
    '''
    向服务发起请求的功能函数
    todo:
        *  可以模仿blockly2sensor_server的response结构
    '''
    #payload is {}
    r = requests.post(url, data=payload)
    #判断通信是否正常
    if r.status_code == 200: #,yes
        #print r
        return r.json()
    else:
        return {'reponse':'error'}



def chat(query):
    '''
    query 是查询字符串
    todo:
        *  判断，当`匹配度`不高的时候，使用turing
    '''
    url = local_server_base_url+"/chat"
    payload = {}
    payload["query"] = query
    response = request_post(url,payload)
    return response["reponse"]

def train(corpus_strings):
    '''
    参数：
        *  corpus_strings:空格分割的字符串
    对话长度不可知，使用post传
    '''
    url = local_server_base_url+"/train"
    payload = {}
    payload["corpus_strings"] = corpus_strings
    response = request_post(url,payload)
    print(response["reponse"]) #print的内容将返回到blockly前端，视为控制台输出

