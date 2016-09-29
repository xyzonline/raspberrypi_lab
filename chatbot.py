#!/usr/bin/env python
# encoding: utf-8
# 需要python3
# open bot
#https://github.com/wwj718/wechat_bot/
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#from chatterbot.training.trainers import ListTrainer
from chatterbot.trainers import ListTrainer
import re

deepThought = ChatBot("deepThought")
deepThought.set_trainer(ListTrainer)
#deepThought.set_trainer(ChatterBotCorpusTrainer)
# 使用中文语料库训练它
# 只需要训练一次，不需要每次启动进程都训练，训练结果默认存到本地`./database.db`,之后启动进程会使用这个数据库


def chat(query):
    # 判断，当匹配度不高的时候，使用turing
    answer = deepThought.get_response(query).text
    return answer

def train(corpus_strings):
    # 训练机器人 ,逗号分隔也行，行分隔
    # 对话列表
    # 案例
    # deepThought.train
    # 假设传进来的就是纯文本，切割它们
    '''
    ["嗳，渡边君，真喜欢我?",
    "那还用说?",
    "那么，可依得我两件事?",
    "三件也依得",
    ]
    '''

    corpus = re.split(r"\s+",corpus_strings) #切割1-n个空格 ,贪婪
    deepThought.train(corpus)


def main():
    deepThought.train("chatterbot.corpus.chinese")  # 语料库 , 不需要反复训练，在python chatbot.py --train=chinene 就好
    pass

if __name__ == '__main__':
    #main()
    corpus=["嗳，渡边君，真喜欢我?","那还用说?"]
    train(corpus)
    print(deepThought.get_response('渡边君'))


