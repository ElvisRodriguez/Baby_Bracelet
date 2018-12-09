'''
Module to extract data from ArduinoUNO's heartbeat sensor.
'''

import random
import serial
import time

from time_stamp import TimeStamp

PORT = '/dev/ttyACM0'
RATE = 9600

def create_serial_obj(port, rate=9600):
	'''
		Description:
			Creates a Serial object.
		Args:
			port: String representing the device name dependent on OS.
			rate (optional): Integer representing the Baud rate of serial_obj.
		Exceptions Raised:
			ValueError: Raised when rate is out of range.
			SerialException: Raised when port cannot be found and/or configured.
		Returns:
			A Serial object with specified port and rate.
	'''
	serial_obj = serial.Serial(port=port, baudrate=rate)
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
				time_stamp = TimeStamp('EST')
				time_stamp = time_stamp.time()
				value_pair = [input_value, time_stamp]
				yield value_pair
			except ValueError:
				continue

def create_fake_value():
	'''
		Mock method of retrieve_serial_value() use for testing only.
	'''
	while True:
		input_value = random.randint(110, 130)
		time_stamp = TimeStamp('EST')
		time_stamp = time_stamp.time()
		value_pair = [input_value, time_stamp]
		yield value_pair


if __name__ == '__main__':
	# Driver code to test if data is being accurately read from the sensor.
	serial_obj = create_serial_obj(port=PORT, rate=RATE)
	sensor_data = retrieve_serial_value(serial_obj)
	while True:
		print(sensor_data.__next__())
