#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import RPi.GPIO as GPIO
import time
import threading #多进程  主进程会等待子进程结束 子进程可以多个
import socket

GPIO.setmode(
    GPIO.BCM
)  #统一引脚形式 ,都用GPIO #引脚图 http://blog.chinaunix.net/attachment/201412/14/21658993_1418547950hA26.png
TRIG = 24
ECHO = 23

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

lock = threading.Lock()


def get_distance():
    '''
    获取障碍物距离
    '''
    #lock.acquire()
    GPIO.output(TRIG, 0)
    time.sleep(0.01)

    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)
    start = time.time()

    while GPIO.input(ECHO) == 0:
        start = time.time()

    while GPIO.input(ECHO) == 1:
        stop = time.time()

    distance = (stop - start) * 340 * 100 / 2  #声波的速度是340m/s
    return '%0.2f' % distance
    lock.release()
    return distance

global get_distance

# socket
host = 'localhost'
port = 6000
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在客户端开启心跳维护
#client.connect((host, port))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def get_fire():
  while True:
     print("begin_get_dis")
     inputValue = get_distance()
     print(inputValue) # 一直循环会出问题
     if inputValue > 50:
        print(inputValue)
        sock.sendto('run', (host,port))
     else:
        print("<50")
        sock.sendto('xxxxx', (host,port))
        time.sleep(0.1)

print('thread %s is running...' % threading.current_thread().name)# 主进程
t1 = threading.Thread(target=get_fire, name='fire')
t1.setDaemon(True)
t1.start()
#t1.join() # 阻塞正在调用的线程
#t2.join()
# 无法kill http://www.jb51.net/article/35165.htm
while True:
    time.sleep(0.1)


