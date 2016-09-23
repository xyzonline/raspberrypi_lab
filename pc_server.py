#!/usr/bin/env python
# encoding: utf-8
# 包含相对路径的代码不能被执行只能被引用
from __future__ import unicode_literals
from flask import Flask
import subprocess
#import get_hostname
app = Flask(__name__)
from threading import Timer
import local
from flask import request

@app.route('/study')
def study():
    print('to study')
    command = ["open","/Applications/iBooks.app"] #打开ibook，可替换为其他
    subprocess.call(command)
    return 'study'

@app.route('/play')
def play():
    command = ["play","/tmp/recording.wav"]
    subprocess.call(command)
    return '播放成功!'




kill = lambda process: process.kill()
@app.route('/sox')
def sox():
    # record
    # 控制程序运行时长
    # 录音3秒
    # https://dzone.com/articles/python-101-how-to-timeout-a-subprocess
    command = ["sox","-d","/tmp/recording.wav"]
    sox = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    my_timer = Timer(3, kill, [sox])
    try:
        my_timer.start()
        stdout, stderr = sox.communicate()
    finally:
        #print (stdout, stderr)
        my_timer.cancel()
        return '录音成功!'

@app.route('/say')
def say():
    #需要传递内容
    content = request.args.get('content')
    #content = '把手拿开'
    access_token = local.access_token
    url = "http://tsn.baidu.com/text2audio?tex={content}&lan=zh&per=0&pit=9&spd=6&cuid=wwj_pi&ctp=1&tok={access_token}".format(content=content,access_token=access_token)
    subprocess.call(['mpg123',url])
    return '说话成功！'


if __name__ == '__main__':
    #sox()
    app.run(host='0.0.0.0',port='5000')
