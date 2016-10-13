#!/usr/bin/env python
# encoding: utf-8
# 包含相对路径的代码不能被执行只能被引用
from __future__ import unicode_literals
from flask import Flask
import flask
import subprocess
#import get_hostname
app = Flask(__name__)
from threading import Timer
import local
from flask import request


#写mac和window客户端，只要是录音和播音模块


@app.route('/study')
def study():
    print('to study')
    command = ["open","/Applications/iBooks.app"] #打开ibook，可替换为其他
    subprocess.call(command)
    return 'study'

@app.route('/play')
def play():
    #http://127.0.0.1:5000/play
    command = ["play","./data/recording.wav"]
    subprocess.call(command)
    return '播放成功!'



kill = lambda process: process.kill()
@app.route('/sox')
def sox():
    # record
    # 控制程序运行时长
    # 录音3秒
    # https://dzone.com/articles/python-101-how-to-timeout-a-subprocess
    # 开始录音，说个声音
    # 录音时长
    #http://127.0.0.1:5000/sox?delay=3
    delay = int(request.args.get('delay',3)) #get 传参,录音时长
    play_mp3("./data/begin_recording.mp3")
    command = ["sox","-d","./data/recording.wav"]
    sox = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    my_timer = Timer(delay, kill, [sox])
    try:
        my_timer.start()
        stdout, stderr = sox.communicate()
    finally:
        #print (stdout, stderr)
        play_mp3("./data/end_recording.mp3")
        my_timer.cancel()
        return '录音成功!'


def play_mp3(uri):
    subprocess.call(['mpg123',uri])


def text2audio_url(content):
    access_token = local.baidu_access_token
    url = "http://tsn.baidu.com/text2audio?tex={content}&lan=zh&per=0&pit=9&spd=6&cuid=wwj_pi&ctp=1&tok={access_token}".format(content=content,access_token=access_token)
    print(url) #录音 开始录音 结束录音，存下
    return url


@app.route('/say')
def say():
    #需要传递内容
    content = request.args.get('content')
    #content = '把手拿开'
    play_mp3(text2audio_url(content))
    return '说话成功！'


if __name__ == '__main__':
    #sox()
    app.run(host='0.0.0.0',port='5000')
