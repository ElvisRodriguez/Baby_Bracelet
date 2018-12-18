import random
import requests
import time

import heartBeats


STATUS_OK = requests.codes.ok
URL = 'https://elvisrodriguez.pythonanywhere.com/data'


def send_heartbeat_data(url=URL):
    '''Sends heartbeat sensor data to Atawear web server.

    Args:
        url: url of web server (type: string).
    Exceptions Raised:
        RuntimeError: Script will fallback to sending dummy data if sensor is
                      not connected to this script's device.
    Returns:
        None.
    '''
    payload = dict()
    get_url = requests.get(url)
    heart_data = heartBeats.read_heart_data()
    while True:
        if get_url.status_code == STATUS_OK:
            sensor_data = next(heart_data)
            beats_per_min = sensor_data[0]
            interbeat_intervals = sensor_data[1]
            payload['heartbeat'] = beats_per_min
            payload['rr_intervals'] = ':'.join(
                [str(interval) for interval in interbeat_intervals]
            )
            post_data = requests.post(url, data=payload)
            if post_data.status_code != STATUS_OK:
                print('Error connecting to server...killing...')
                break

def create_dummy_data():
    '''
    This method creates dummy data for testing purposes only.
    Do not use in production.
    '''
    value = random.randint(95,105)
    while True:
        interval = [x for x in range(595,605)]
        yield (value, interval)

def fallback(delay=1):
    '''
    This method sends dummy data for testing purposes only.
    Do not use in production.
    '''
    payload = dict()
    get_url = requests.get(URL)
    while True:
        dummy_data = create_dummy_data()
        if get_url.status_code == STATUS_OK:
            data = next(dummy_data)
            payload['heartbeat'] = data[0]
            intervals = ':'.join([str(x) for x in data[1]])
            payload['rr_intervals'] = intervals
            post_data = requests.post(URL, data=payload)
            if post_data.status_code == STATUS_OK:
                print('Sending {n} to {url}'.format(n=data[0], url=URL))
                time.sleep(delay)
            get_data = requests.get(URL, params=payload)
            print('Got Back {data}'.format(data=get_data.url))


if __name__ == '__main__':
    try:
        send_heartbeat_data()
    except RuntimeError:
        print('Environment setup for script is incomplete.')
        print('Running dummy script instead...')
        time.sleep(0.5)
        fallback(delay=1)
