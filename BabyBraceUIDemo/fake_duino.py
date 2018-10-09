import collections
import datetime
import random
import time

from time_stamp import *

def create_fake_values():
    counter = 0
    data = list()
    while True:
        input_value = random.randint(60, 80)
        time_stamp = create_timestamp()
        time_stamp = format_timestamp(time_stamp)
        data.append((input_value, time_stamp))
        counter += 1
        #time.sleep(1)
        if counter == 60:
            bpms = [item[0] for item in data]
            timestamps = [item[1] for item in data]
            return [timestamps, bpms]

if __name__ == '__main__':
    create_fake_values()
