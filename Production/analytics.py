'''
Data Analytics module for determining concerning heart rate patterns.
'''

def average_heartbeat(data):
    return sum(data) // len(data)

def spike_or_dip(data):
    if len(data) < 50:
        return 'insufficient data'
    notification_threshold = len(data) // 5
    index = 1
    while index < len(data):
        count = 0
        while data[index] < data[index-1] and index < len(data):
            count += 1
            index += 1
        if count >= notification_threshold:
            return 'spike'
        else:
            count = 0
        while data[index] > data[index-1] and index < len(data):
            count += 1
            index += 1
        if count >= notification_threshold:
            return 'dip'
        else:
            count = 0
        index += 1
