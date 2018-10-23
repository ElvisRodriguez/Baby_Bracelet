'''
Module to extract data from ArduinoUNO's heartbeat sensor.
'''

import random
import serial
import time
from time_stamp import *

PORT = '/dev/ttyACM0'
RATE = 9600

# TODO(Joel): Check if Args description of create_serial_obj() method is accurate
def create_serial_obj(port, rate):
	'''
		Description:
			Creates a Serial object.
		Args:
			port: String representing the port of the ArduinoUNO's heartbeat
				  data.
			rate: Integer representing that rate at which data is serialized.
		Exceptions Raised:
			Undefined.
		Returns:
			A Serial object with specified port and rate.
	'''
	serial_obj = serial.Serial(port,rate)
	return serial_obj

def retrieve_serial_value(serial_obj):
	'''
		Description:
			Reads and formats sensor data recieved by a serial object.
		Args:
			serial_obj: A Serial object containing sensor data.
		Exceptions Raised:
			AttributeError: Raised if input is not a Serial object.
		Returns:
			A generator object containing the most current sensor data.
	'''
	serial_obj.flushInput()
	while True:
		if serial_obj.inWaiting() > 0:
			input_value = serial_obj.readline()
			try:
				input_value = int(input_value)
				time_stamp = create_timestamp()
				time_stamp = current_hour(time_stamp)
				value_pair = [input_value, time_stamp]
				yield value_pair
			except ValueError:
				continue

if __name__ == '__main__':
	# Driver code to test if data is being accurately read from the sensor.
	serial_obj = create_serial_obj(port=PORT, rate=RATE)
	sensor_data = retrieve_serial_value(serial_obj)
	while True:
		print(sensor_data.__next__())
