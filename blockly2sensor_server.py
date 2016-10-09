#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
import sys;reload(sys);sys.setdefaultencoding('utf8')
import subprocess
import time
import flask
import base64
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

# 本地硬件模块



app = Flask(__name__)
CORS(app)
KEY = 'test' #写成装饰器
# 你应该把用户假设为可信的，毕竟是他自己的树莓派 ,所以代码可信
codefile = './codetest.py'

def save_code(code):
    with open(codefile, 'w+') as codetest: # open or create
        codetest.write(code)

    # 存下后运行好了。存为本地codetest.py
    # 上下文可控

@app.route('/run',methods=['POST']) #post code Base64编码 http://blog.just4fun.site/decode-and-encode-note.html
def run_code():
    # 接受代码，存为指定目录文件：./begin,然后用subprocess运行，权限是继承shell的（sudo）,约定好结构，调用函数即可,循环之类的都可以写，块里只包含最干净的
    #健壮，没有的话，用户无法进入
    #code_base64 = request.form.get('code','') #表单形式提交，写个httpie demo
    code =  request.get_json().get('code')
    key =  request.get_json().get('key')
    #code=base64.b64decode(code_base64) # .decode("utf-8") #尴尬在于只有那一部分是编码的
    print code
    # 硬件模块
    pi_module = "import distance,send_emails,chatbot,cloud_ai\n"
    code = "#coding:utf-8\nimport sys;reload(sys);sys.setdefaultencoding('utf8')\n"+pi_module+code
    #key = request.form.get('key','') #表单形式提交，写个httpie demo
    if key != KEY:
        return flask.jsonify({"error":'key error'})

    # http -f post  192.168.0.115:5000/run code='print "hello"' key='test'
    response = {}
    response['code'] = code
    save_code(code)
    # 如果把下边方法包装到函数里，会报错说栈太深, RuntimeError: maximum recursion depth exceeded
    try:
        # 使用flake8，pylint 更好的options
        #subprocess.check_output(["pyflakes",codefile],stderr=subprocess.STDOUT) # 不用静态交叉，直接运行把
        # 运行之前清理其他 python codetest.py  # sudo ps aux |grep codetest
        #pkill -f codetest.py
        subprocess.call(["pkill","-f",codefile])
        code_result = subprocess.check_output(["python",codefile]) #实际运行代码，保证单线程运行，kill其他codetest.py的进程，有root权限
        run_message = '运行成功'
        response['code_result'] = code_result
    except subprocess.CalledProcessError,e:
        run_message = '运行失败'
        response['error'] = e.output
        # 在client print error 即可看到细节
    result = run_message
    # run it  , subpro
    response['info'] = result
    #
    # 实际是在代码中调用代码，运行字符串为代码,ast
    return flask.jsonify(response)


@app.route('/access',methods=['GET']) #post code Base64编码 http://blog.just4fun.site/decode-and-encode-note.html
def acccess():
    response = {}
    return flask.jsonify(response)

# 最后清理GPIO口（不做也可以，建议每次程序结束时清理一下，好习惯）
#RPi.GPIO.cleanup()


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')
    # gunicorn
    # sudo gunicorn blockly2sensor_server:app --bind 0.0.0.0:5000 -w 4
