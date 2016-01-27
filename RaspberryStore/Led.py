#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
#���Ų���BCM����
GPIO.setmode(GPIO.BCM)
#����һ�����飬���ζ�Ӧ8���Ƶ�����BCM����
pins = [5, 6, 13, 19, 0, 1, 7, 8] #GPIO ports
#����SAKS����ɫLED������ܹ������ţ��˴��������λѡ�رգ�ֻ���ź�������LED
GPIO.setup(17, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(27, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(22, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(10, GPIO.OUT, initial=GPIO.HIGH)
#����һ����ݵ��������ŵķ���
def setp(n, status='off'):
    if status == 'on':
        GPIO.output(n, GPIO.LOW)
    else:
        GPIO.output(n, GPIO.HIGH)
#�������飬��������8��LED���ų�ʼ��
for i in pins:
    GPIO.setup(i, GPIO.OUT)
    setp(i, 'off')

try:
    #��ǰ����������LED�������е�λ��
    i = 0
    while True:
    	#���������е�i��LED
    	setp(pins[i], 'on')
    	#��ʱ0.1��
        time.sleep(0.1)
    	#Ϩ�������е�i��LED
    	setp(pins[i], 'off')
    	#�ı�i��ʹ֮��Ӧ����һ��LED������Ѿ������һ��LED�����Ӧ����1��LED
    	i += 1
    	if i == len(pins):
    		i = 0
except:
    print "except"
    GPIO.cleanup()