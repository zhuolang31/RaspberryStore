#!/usr/bin/env python
# -*- coding: utf-8 -*-
#���� SAKS SDK ģ��
from sakshat import SAKSHAT
import time
import commands

#Declare the SAKS Board������һ��SAKS����
SAKS = SAKSHAT()

#���ظ����͵�CPU�¶�
def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp) / 1000
    #�������ʹ�û����¶ȣ���ע��
    #return float(1.8*cpu_temp)+32

#���������
if __name__ == "__main__":
    while True:
        t = get_cpu_temp()
        #�����ϣ��ʵʱ�¶ȵ���ֵ�������Ļ����ȡ�������ע��
        #print("%.2f" % t)
        #����SAKS������ܶ���(digital_display)����������ָ����ʽ��ʾ(show)�¶���ֵ
        SAKS.digital_display.show("%.2f" % t)
        #������ʱ�趨Ϊ50�Ⱦ�������
        if t > 50:
            #����SAKS�ķ���������(buzzer)���������հ���һ����Ƶ�ʷ�������(beepAction)������Ĳ�������2����ļ������30��
            SAKS.buzzer.beepAction(0.02,0.02,30)
        time.sleep(1)

    input("Enter any keys to exit...")