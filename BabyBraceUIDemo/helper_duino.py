import collections
import datetime
import random
import time

from time_stamp import *

def format_value(value_pair):
    return '{bpm} {ts}\n'.format(bpm=value_pair[0], ts=value_pair[1])

def write_output(value_pairs):
    with open('output.txt', 'w') as file:
        for pair in value_pairs:
            file.write(pair)
        file.close()

def read_data_values():
    time_stamps = []
    heart_rate = []
    with open('output.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            line = line.split()
            heart_rate.append(int(line[0]))
            time_stamps.append(line[2].replace('\n', ''))
    return [time_stamps, heart_rate]

def create_fake_values():
    data = collections.deque()
    while True:
        input_value = random.randint(80, 160)
        time_stamp = create_timestamp()
        time_stamp = format_timestamp(time_stamp)
        value_pair = format_value([input_value, time_stamp])
        data.append(value_pair)
        if len(data) > 60:
            data.popleft()
        elif len(data) == 60:
            write_output(data)
        time.sleep(1)
