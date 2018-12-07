import time_stamp

def render_data(heart_rates, timestamps, data):
    if int(data) > 0:
        heart_rates.append(int(data))
        ts = time_stamp.TimeStamp('EST')
        timestamps.append(ts.time())
