#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import RPi.GPIO as GPIO
import time
import threading #多进程  主进程会等待子进程结束 子进程可以多个
import socket

pin=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN)
inputValue = 1 # 高电平.电阻小，正常状态 # 异常电阻升高

# socket
host = 'localhost'
port = 6000
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在客户端开启心跳维护
#client.connect((host, port))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def ask_help():
    print("run")
    #client.send('run')
    sock.sendto('run', (host,port))
    time.sleep(0.05)

def hello():
    while True:
        # 使用UDP
        sock.sendto('xxx\n', (host,port))
        #client.send('xxx\n')
        print("xxx\n")
        time.sleep(0.05)
def get_fire():
  global inputValue #多线程需要这样
  while True:
     # 循环吧，会不会卡死
     # 在一段时间内搜集
     #只能是一直循环
     # 事件驱动 多线程  或者单线程非阻塞
     #print("get_fire...")
     inputValue =GPIO.input(pin)
     if inputValue==0:
        #print(inputValue)
        ask_help()
        #time.sleep(0.1)

print('thread %s is running...' % threading.current_thread().name)# 主进程
t1 = threading.Thread(target=get_fire, name='fire')
t1.setDaemon(True)
t2 = threading.Thread(target=hello, name='hello')
t2.setDaemon(True)
t1.start()
t2.start()
#t1.join() # 阻塞正在调用的线程
#t2.join()
# 无法kill http://www.jb51.net/article/35165.htm
while True:
    pass
