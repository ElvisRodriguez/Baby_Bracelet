import random
import serial
import time
from time_stamp import *

def create_serial_obj(port, rate):
	serial_obj = serial.Serial(port,rate)
	return serial_obj

def create_fake_value():
	while True:
		input_value = random.randint(80, 160)
		time_stamp = create_timestamp()
		time_stamp = format_timestamp(time_stamp)
		time_stamp = time_stamp.split()
		value_pair = [input_value, time_stamp[1]]
		yield value_pair

def retrieve_serial_value(serial_obj):
	serial_obj.flushInput()
	while True:
		if serial_obj.inWaiting() > 0:
			input_value = serial_obj.readline()
			try:
				input_value = int(input_value)
				time_stamp = create_timestamp()
				time_stamp = format_timestamp(time_stamp)
				value_pair = [input_value, time_stamp]
				yield value_pair
			except ValueError:
				continue

if __name__ == '__main__':
	serial_obj = create_serial_obj(port='/dev/ttyACM0', rate=9600)
	sensor_data = retrieve_serial_value(serial_obj)
	while True:
		print(sensor_data.__next__())
