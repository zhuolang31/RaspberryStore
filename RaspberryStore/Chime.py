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

while True:
    # ���´����ȡϵͳʱ�䡢ʱ���֡��롢���ڵ���ֵ
    t = time.localtime()
    h = t.tm_hour
    m = t.tm_min
    s = t.tm_sec
    w = time.strftime('%w',t)
    #print h,m,s,w
    time.sleep(0.3)
    # �ж��Ƿ�Ϊ����
    if m == 0 and s == 0:
        # ����ע�Ͳ��������ñ�ʱ�Ľű��������������գ�˯�����������²����ף�
        #if w==0 or w==6:
        #    continue
        # ���´����жϵ�ʱ�������22�������8���ڼ䲻��ʱ����Ӱ��˯��
        if h > 22 or h < 8:
            continue
        # Сʱ��N����12�������£���N-12��
        if h > 12:
            h = h - 12
        beepAction(0.3, 0.5, h)
        time.sleep(1)
    # �ж��Ƿ�Ϊ30��
    if m == 30 and s == 0:
        if h > 22 or h < 8:
            continue
        # �������2��
        beepAction(0.05, 0.05, 2)
        time.sleep(1)
   #�ж��Ƿ�Ϊ20��
   if m == 20:
       beepAction(0.05,0.05,2)
       time.sleep(1)