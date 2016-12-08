#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time

lightPin = 4  # GPIO Pin 18
servoPin = 18 # GPIO Pin 18

GPIO.setmode(GPIO.BCM)

# Setup servo pin status
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 100)
pwm.start(0)

def servo_set(angle):
    #for i in range(0,181,10):
    #pwm.ChangeDutyCycle(angle) #设置转动角度
    #pwm.ChangeDutyCycle(2.5 + 10 * (angle) / 180)
    duty  = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    #pwm.ChangeDutyCycle(5 ) #设置转动角度
    time.sleep(0.02)                      #等该20ms周期结束
    pwm.ChangeDutyCycle(0)                  #归零信号
    time.sleep(0.2)

def open():
    servo_set(30)
    servo_set(30)
def close():
    #time.sleep(1)
    servo_set(180-30)
    servo_set(180-30)
    #time.sleep(1)
    #servo_set(30)

#time.sleep(3)
open()
time.sleep(1)
close()
