#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) #统一引脚形式 ,都用GPIO 23，24    #http://blog.chinaunix.net/attachment/201412/14/21658993_1418547950hA26.png

TRIG = 24 #18 # GPIO.setmode(GPIO.BOARD)
ECHO = 23 #16

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
# 获取障碍物距离
# 这个实际上只有输出没有输入,是一个类似数值的东西
def get_distance():
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

        distance = (stop - start) * 340*100 / 2 #声波的速度是340m/s
        #print str(distance) +" cm"
        #print 'Distance: %0.4f cm' % distance
        return distance # 很多位的小数

