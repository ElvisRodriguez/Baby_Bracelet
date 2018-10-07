#!/usr/bin/env python
import serial
port = "/dev/ttyACM0"
rate = 9600
s1 = serial.Serial(port,rate)
s1.flushInput()


while True:
	if s1.inWaiting()>0:
		inputValue = s1.readline()
		print(inputValue)
