#!/usr/bin/env python
# encoding: utf-8

#!/usr/bin/env python


import RPi.GPIO as GPIO
import time
import signal
import atexit

atexit.register(GPIO.cleanup)

servopin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin,50) #50HZ
p.start(0)
time.sleep(2)


def set_angle(angle):
  j = 0
  for i in range(0,180,10):
    p.ChangeDutyCycle(2.5+10 * i / 180) #设置转动角度
    time.sleep(0.02)                      #等该20ms周期结束
    p.ChangeDutyCycle(0)                  #归零信号
    time.sleep(0.2)
    j = j +  10
    if j > angle :
        break
  k = 180
  for i in range(180,0,-10):
    p.ChangeDutyCycle(2.5+10 * i / 180) #设置转动角度
    time.sleep(0.02)
    p.ChangeDutyCycle(0)
    time.sleep(0.2)
    k = k - 10
    if k < (180-angle):
        break
set_angle(90)
