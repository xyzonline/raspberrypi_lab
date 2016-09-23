#!/usr/bin/env python
# encoding: utf-8
# 包含相对路径的代码不能被执行只能被引用
from flask import Flask
import subprocess
import get_hostname
app = Flask(__name__)

@app.route('/study')
def study():
    print('to study')
    command = ["open","/Applications/iBooks.app"] #打开ibook，可替换为其他
    subprocess.call(command)
    return 'study'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')
