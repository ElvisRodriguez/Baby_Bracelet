'''
Helper method to place POST data into the appropriate data containers.
'''

import time_stamp


def render_data(heart_rates, timestamps, extended_heart_rates, bpm_data,
                interbeat_intervals, rr_intervals):
    '''Formats heart data to include in data queues.

    Args:
        heart_rates: heartbeat values (type: collections.deque(int)).
        timestamps: timestamps (type: collections.deque(string)).
        extended_heart_rates: extension of heart_rates
                              (type: collections.deque(int)).
        bpm_data: heartbeat data (type: numeric string).
        interbeat_intervals: collection of rr_intervals
                             (type: collections.deque(int)).
        rr_intervals: intervals between heartsbeats in milliseconds
                      (type: colon-delimited string).
    Raises:
        ValueError if inputs are not of aforementioned type (or similar).
    Returns:
        None.
    '''
    if type(bpm_data) == type(int) and bpm_data > 0:
        heart_rates.append(data_as_integer)
        extended_heart_rates.append(data_as_integer)
        ts = time_stamp.TimeStamp('EST')
        timestamps.append(ts.time())
    if type(rr_intervals) == type(str) and rr_intervals != '':
        rr_intervals = rr_intervals.split(':')
        rr_intervals = [int(interval) for interval in rr_intervals]
        interbeat_intervals.extend(rr_intervals)
