#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
import subprocess
import time
import flask
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)
KEY = 'test' #写成装饰器
# 你应该把用户假设为可信的，毕竟是他自己的树莓派 ,所以代码可信
codefile = './codetest.py'

def save_code(code):
    with open(codefile, 'w+') as codetest: # open or create
        codetest.write(code)

    #存下后运行好了。存为本地codetest.py
    # exec eval 对比，测试环境，真实运行不要用这个
    # 上下文可控
    # exec语句不会返回任何对象。而eval会返回表达式的值。
    # 表达式是 某事，语句是 做某事（即告诉计算机做什么)

# 循环10次
@app.route('/run',methods=['POST']) #post code Base64编码 http://blog.just4fun.site/decode-and-encode-note.html
def run_code():
    # 添加密码
    # 接受代码，存为指定目录文件：./begin,然后用subprocess运行，权限是继承shell的（sudo）,约定好结构，调用函数即可,循环之类的都可以写，块里只包含最干净的
    #健壮，没有的话，用户无法进入
    code = request.form.get('code','') #表单形式提交，写个httpie demo
    key = request.form.get('key','') #表单形式提交，写个httpie demo
    if key != KEY:
        return flask.jsonify({"error":'key error'})

    # http -f post  192.168.0.115:5000/run code='print "hello"' key='test'
    response = {}
    response['code'] = code
    save_code(code)
    # 如果把下边方法包装到函数里，会报错说栈太深, RuntimeError: maximum recursion depth exceeded
    try:
        subprocess.check_output(["pyflakes",codefile],stderr=subprocess.STDOUT)
        run_message = '运行成功'

        # 运行成功的
    except subprocess.CalledProcessError,e:
        run_message = '运行失败'
        response['error'] = e.output
        # 在client print error 即可看到细节
    result = run_message
    # run it  , subpro
    response['result'] = result
    #
    # 实际是在代码中调用代码，运行字符串为代码,ast
    return flask.jsonify(response)

# 最后清理GPIO口（不做也可以，建议每次程序结束时清理一下，好习惯）
#RPi.GPIO.cleanup()


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')