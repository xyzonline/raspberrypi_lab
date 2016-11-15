#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time
import threading #多进程  主进程会等待子进程结束 子进程可以多个


GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
inputValue = 1 # 高电平.电阻小，正常状态 # 异常电阻升高
def ask_help():
    print("fire!help!")

def hello():
    while True:
        pass
        #time.sleep(0.5)
        #print("hello")
def get_fire():
  global inputValue #多线程需要这样
  while True:
     # 循环吧，会不会卡死
     # 在一段时间内搜集
     #只能是一直循环
     # 事件驱动 多线程  或者单线程非阻塞
     #print("get_fire...")
     inputValue =GPIO.input(21)
     if inputValue==0:
        print(inputValue)
        ask_help()
        time.sleep(0.5)

print('thread %s is running...' % threading.current_thread().name)# 主进程
t1 = threading.Thread(target=get_fire, name='fire')
t2 = threading.Thread(target=hello, name='hello')
t1.start()
t2.start()
t1.join()
t2.join()
# 无法kill http://www.jb51.net/article/35165.htm
