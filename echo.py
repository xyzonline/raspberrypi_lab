#!/usr/bin/env python
# encoding: utf-8

# 使用16，18 引脚 echo，trig

import RPi.GPIO as GPIO
import time
import requests
import beep #本地 如何使用相对理解，相对路径不能直接运行
import smile
import  i_am_studing
GPIO.setmode(GPIO.BCM) #统一引脚形式 ,都用GPIO 23，24    #http://blog.chinaunix.net/attachment/201412/14/21658993_1418547950hA26.png

TRIG = 24 #18 # GPIO.setmode(GPIO.BOARD)
ECHO = 23 #16

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def handle():
    print("<100cm")
    print 'bi!'
    a = 2 #第一首曲子
    buzzer = beep.Buzzer()
    buzzer.play(int(a))
    smile.draw_smile()
    i_am_studing.study()

def main():
    try:
      while True:
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
        print 'Distance: %0.4f cm' % distance
        if distance < 100:
            handle()
        time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
