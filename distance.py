#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time
'''
超声波测距模块
'''

GPIO.setmode(
    GPIO.BCM
)  #统一引脚形式 ,都用GPIO #引脚图 http://blog.chinaunix.net/attachment/201412/14/21658993_1418547950hA26.png
TRIG = 24
ECHO = 23

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def get_distance():
    '''
    获取障碍物距离
    '''
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
    #print 'Distance: %0.4f cm' % distance
    return distance  # 精确值，小数数位很多
