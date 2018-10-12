#!/usr/bin/env python
import serial

import helper_duino
from time_stamp import *

def create_serial_obj(port, rate):
	serial_obj = serial.Serial(port,rate)
	return serial_obj

def write_serial_values(serial_obj):
	serial_obj.flushInput()
	data = []
	while len(data) < 60:
		if serial_obj.inWaiting() > 0:
			input_value = serial_obj.readline()
			try:
				input_value = int(input_value)
			except ValueError:
				input_value = None
			time_stamp = create_timestamp()
			time_stamp = format_timestamp(time_stamp)
			if input_value is not None:
				value_pair = helper_duino.format_value([input_value, time_stamp])
			data.append(value_pair)
	helper_duino.write_output(data)

if __name__ == '__main__':
	serial_obj = create_serial_obj(port='/dev/ttyACM0', rate=9600)
	write_serial_values(serial_obj)
