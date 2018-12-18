'''
Data Analytics module for determining concerning heart rate patterns.
'''

import math


def average_heartbeat(data):
    return sum(data) // len(data)

def is_rising(data):
    notification_threshold = len(data) // 5
    count = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            count += 1
        else:
            count = 0
        if count >= notification_threshold:
            return True
    return False

def is_dropping(data):
    notification_threshold = len(data) // 5
    count = 0
    for i in range(1, len(data)):
        if data[i] < data[i-1]:
            count += 1
        else:
            count = 0
        if count >= notification_threshold:
            return True
    return False

def heart_rate_variability(interbeat_intervals):
    N = len(interbeat_intervals)
    mean_square = []
    for i in range(1, N):
        difference = interbeat_intervals[i] - interbeat_intervals[i-1]
        mean_square.append(difference ** 2)
    reciprocal = 1 / (N - 1)
    result = math.sqrt(reciprocal * sum(mean_square))
    return result
