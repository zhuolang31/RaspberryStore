#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys

PIN_NO_BEEP = 11
PIN_NO_LED = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NO_BEEP, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN_NO_LED, GPIO.OUT, initial=GPIO.HIGH)

# ����������LED����
def beep(seconds):
    GPIO.output(PIN_NO_BEEP, GPIO.LOW)
    GPIO.output(PIN_NO_LED, GPIO.LOW)
    time.sleep(seconds)
    GPIO.output(PIN_NO_BEEP, GPIO.HIGH)
    GPIO.output(PIN_NO_LED, GPIO.HIGH)

# ���������LED�����װ��������������ֱ�Ϊ��ռ��ʱ�䡱�Լ��ظ�����
def beepAction(secs, sleepsecs, times):
    for i in range(times):
        beep(secs)
        time.sleep(sleepsecs)

println("start beep")
try:
    while True:
        beep(0.005);
        time.sleep(0.005)

except:
    print "except"
    GPIO.cleanup()