#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
import sys;reload(sys);sys.setdefaultencoding('utf8') #中文编码问题
import subprocess #用于调用外部程序
import flask
from flask import Flask
from flask import request  #处理请求参数
from flask_cors import CORS  #, cross_origin  #跨域请求
import settings
# https://github.com/miguelgrinberg/Flask-SocketIO

# flask websocket
from flask_socketio import SocketIO, emit,send
import time


app = Flask(__name__)
CORS(app)
KEY = settings.APP_KEY
CODE_FILE = settings.CODE_FILE
socketio = SocketIO(app)



def save_code(code):
    '''
    将代码保存为本地文件：CODE_FILE
    '''
    with open(CODE_FILE, 'w+') as codetest: # open or create
        codetest.write(code) # 存为本地codetest.py

# socketio test
@socketio.on('run_code') # 长连接
def test_socket(message):
    #print(type(message))
    #emit('pi_output', {'data': 'hello world (result)!'})
    code = message.get("code")
    key =  message.get("key")
    # 硬件模块,预加载
    # 硬件模块需要sudo权限
    pi_module = "import distance,send_emails,chatbot_client,cloud_ai,pi_media,DHT11\n"
    code = "#coding:utf-8\nimport sys;reload(sys);sys.setdefaultencoding('utf8')\n"+pi_module+code
    #if key != KEY: # 验证密码
    #    return flask.jsonify({"error":'key error'})

    # http post  192.168.0.115:5000/run code='print "hello"' key='test' # 默认是json
    response = {}
    response['code'] = code
    save_code(code)
    # 下边方法不能包装到函数里，否则会报错说栈太深.  RuntimeError: maximum recursion depth exceeded
    try:
        # 使用flake8，pylint 更好的options
        #subprocess.check_output(["pyflakes",CODE_FILE],stderr=subprocess.STDOUT) # 不用静态交叉，直接运行吧
        # 运行之前清理其他 python codetest.py  # sudo ps aux |grep codetest
        #pkill -f codetest.py
        subprocess.call(["pkill","-f",CODE_FILE]) #运行之前把之前运行的停掉,保证每次只运行一个程序
        code_result = subprocess.check_output(["python",CODE_FILE]) #实际运行代码，保证单线程运行，kill其他codetest.py的进程
        running_status = '运行成功'
        response['code_result'] = code_result
    except subprocess.CalledProcessError,e:
        running_status = '运行失败'
        response['error'] = e.output

    response['running_status'] =  running_status
    #return flask.jsonify(response)
    #emit(response)
    emit('pi_output', response)
    '''
    for i in range(1,5):
        #emit('pi_output',{"code_result":"waiting..."}) # 为何会一次返回
        send(response,json=True)
        time.sleep(1)
    '''




@app.route('/run',methods=['POST']) #post code Base64编码 http://blog.just4fun.site/decode-and-encode-note.html
def run_code():
    '''
    入口，接收来自blockly前端页面的请求
    todo:
        *  改为websocket
        *  传感器部分重构,太分散,命名规则不统一

    pi_module说明:
        *  distance: 超声波传感器，测量超声波传感器距离
        *  send_emails: 邮件模块
        *  chatbot_client:
        *  cloud_ai: 云端ai，turing bot
        *  pi_media: media相关，音频
        *  DHT11: 温度传感器
    '''
    code =  request.get_json().get('code') # 使用json传输数据
    key =  request.get_json().get('key')
    # 硬件模块,预加载
    # 硬件模块需要sudo权限
    pi_module = "import distance,send_emails,chatbot_client,cloud_ai,pi_media,DHT11\n"
    code = "#coding:utf-8\nimport sys;reload(sys);sys.setdefaultencoding('utf8')\n"+pi_module+code
    if key != KEY: # 验证密码
        return flask.jsonify({"error":'key error'})

    # http post  192.168.0.115:5000/run code='print "hello"' key='test' # 默认是json
    response = {}
    response['code'] = code
    save_code(code)
    # 下边方法不能包装到函数里，否则会报错说栈太深.  RuntimeError: maximum recursion depth exceeded
    try:
        # 使用flake8，pylint 更好的options
        #subprocess.check_output(["pyflakes",CODE_FILE],stderr=subprocess.STDOUT) # 不用静态交叉，直接运行吧
        # 运行之前清理其他 python codetest.py  # sudo ps aux |grep codetest
        #pkill -f codetest.py
        subprocess.call(["pkill","-f",CODE_FILE]) #运行之前把之前运行的停掉,保证每次只运行一个程序
        code_result = subprocess.check_output(["python",CODE_FILE]) #实际运行代码，保证单线程运行，kill其他codetest.py的进程
        running_status = '运行成功'
        response['code_result'] = code_result
    except subprocess.CalledProcessError,e:
        running_status = '运行失败'
        response['error'] = e.output

    response['running_status'] =  running_status
    return flask.jsonify(response)


@app.route('/access',methods=['GET'])
def access():
    '''
    检查网络是否通畅，服务是否正常
    '''
    response = {}
    return flask.jsonify(response)

# 最后清理GPIO口（不做也可以，建议每次程序结束时清理一下，好习惯）
#RPi.GPIO.cleanup()


if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0",port=5005)
    # sudo gunicorn blockly2sensor_server:app --bind 0.0.0.0:5000 -w 1
    # sudo python websocket_blockly2sensor_server.py
