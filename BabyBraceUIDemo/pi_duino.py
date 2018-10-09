#!/usr/bin/env python
import serial
from time_stamp import *

def create_serial_obj(port, rate):
	serial_obj = serial.Serial(port,rate)
	return serial_obj

def read_serial_values(serial_obj):
	serial_obj.flushInput()
	while True:
		if serial_obj.inWaiting() > 0:
			input_value = serial_obj.readline()
			try:
				input_value = int(input_value)
			except ValueError:
				input_value = None
			time_stamp = create_timestamp()
			time_stamp = format_timestamp(time_stamp)
			print(input_value, time_stamp)

if __name__ == '__main__':
	serial_obj = create_serial_obj(port='/dev/ttyACM0', rate=9600)
	read_serial_values(serial_obj)
