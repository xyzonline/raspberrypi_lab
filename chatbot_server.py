#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

from flask import Flask
import flask
#import get_hostname
app = Flask(__name__)
from threading import Timer
from flask import request

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import re
import subprocess

'''
chatterbot本地服务

自动训练语料需要python3，如果是手动训练2/3皆可

只需要训练一次，不需要每次启动进程都训练，训练结果默认存到本地`./database.db`,之后启动进程会使用这个数据库
'''

#deepThought = ChatBot("deepThought",read_only=True) #明确从train中学习
deepThought = ChatBot("deepThought") #从对话中学习
deepThought.set_trainer(ListTrainer)

@app.route('/chat',methods=['POST'])
def chat():
    # 判断，当匹配度不高的时候，使用turing
    # http  POST  http://192.168.0.124:5001/chat query=你好
    query = request.form.get("query","你好")
    answer = deepThought.get_response(query).text
    response = {'reponse':answer}
    return flask.jsonify(response)

@app.route('/train',methods=['POST'])
def train():
    '''
    # 假设传进来的就是纯文本，切割它们,逗号空格
    目标格式:
    ["嗳，渡边君，真喜欢我?",
    "那还用说?",
    "那么，可依得我两件事?",
    "三件也依得",
    ]

    todo:
        *  模仿 blockly2sensor_server使用json传数据
    '''
    corpus_strings = request.form.get("corpus_strings","你好 早啊") #http://stackoverflow.com/questions/10434599/how-can-i-get-the-whole-request-post-body-in-python-with-flask
    corpus = re.split(r"\s+",corpus_strings) #切割1-n个空格 ,贪婪
    deepThought.train(corpus)
    response = {'reponse':'train ok'}
    return flask.jsonify(response)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5001')

