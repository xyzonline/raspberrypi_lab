#!/usr/bin/env python
# encoding: utf-8

# chatbot client
# 请求chatbot server
import requests


localhost = "127.0.0.1"
local_server_base_url = 'http://{}:5001'.format(localhost)

def request_post(url,payload):
    #payload is {}
    r = requests.post(url, data=payload)
    #判断通信是否正常
    if r.status_code == 200: #,yes
        #print r
        return r.json()
    else:
        {'reponse':'error'}
    # {'reponse':'train ok'}



def chat(query):
    '''
    query 是查询字符串
    '''
    # 判断，当匹配度不高的时候，使用turing
    #answer = deepThought.get_response(query).text
    url = local_server_base_url+"/chat"
    #print(url)
    payload = {}
    payload["query"] = query
    response = request_post(url,payload)
    #print(response)
    return response["reponse"]

def train(corpus_strings):
    '''
    corpus_strings 空格分割的字符串
    对话长度不可知，使用post传
    '''
    url = local_server_base_url+"/train"
    payload = {}
    payload["corpus_strings"] = corpus_strings
    response = request_post(url,payload)
    print(response["reponse"])

