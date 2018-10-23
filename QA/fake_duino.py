import random
import time
from time_stamp import *


def create_fake_value():
	while True:
		input_value = random.randint(80, 160)
		time_stamp = create_timestamp()
		time_stamp = format_timestamp(time_stamp)
		time_stamp = time_stamp.split()
		value_pair = [input_value, time_stamp[1]]
		yield value_pair
