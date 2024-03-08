#!/usr/bin/env python3
import serial
import time


ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
ser.setDTR(False)
time.sleep(1)
ser.flushInput()
ser.setDTR(True)
time.sleep(2)


def sonoUnaFnCarinaCaruccia(a):
    ser.write(a)

def read_serial():
    line = ser.readline().decode('utf-8')
    if line!="":
       print(line)
    
    
    
    


        