'''
Helper method to place POST data into the appropriate data containers.
'''

import time_stamp


def render_data(heart_rates, timestamps, data, extended_data):
    '''Formats heartbeat value to include in data queues.

    Args:
        heart_rates: heartbeat values (type: collections.deque(int)).
        timestamps: timestamps (type: collections.deque(string)).
        data: heartbeat data (type: numeric string).
        extended_data: extension of heart_rates (type: collections.deque(int)).
    Raises:
        ValueError if inputs are not of aforementioned type (or similar).
    Returns:
        None.
    '''
    data_as_integer = int(data)
    if data_as_integer > 0:
        heart_rates.append(data_as_integer)
        extended_data.append(data_as_integer)
        ts = time_stamp.TimeStamp('EST')
        timestamps.append(ts.time())
