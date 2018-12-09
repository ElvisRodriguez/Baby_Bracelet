import random
import requests
import time

import heartBeats


STATUS_OK = requests.codes.ok
URL = 'https://elvisrodriguez.pythonanywhere.com/data'
POST_FIELD = 'heartbeat'


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
    heart_rates = heartBeats.read_heart_rates()
    while True:
        if get_url.status_code == STATUS_OK:
            heart_rate = next(heart_rates)
            payload['heartbeat'] = heart_rate
            post_data = requests.post(url, data=payload)
            if post_data.status_code == STATUS_OK:
                print('Sending: {data} to server'.format(data=heart_rate))

def create_dummy_data():
    '''
    This method creates dummy data for testing purposes only.
    Do not use in production.
    '''
    value = random.randint(95,105)
    while True:
        yield value

def fallback(delay=1):
    '''
    This method sends dummy data for testing purposes only.
    Do not use in production.
    '''
    get_url = requests.get(URL)
    while True:
        dummy_data = create_dummy_data()
        if get_url.status_code == STATUS_OK:
            data = next(dummy_data)
            post_data = requests.post(URL, data={'heartbeat':data})
            if post_data.status_code == STATUS_OK:
                print('Sending {n} to {url}'.format(n=data, url=URL))
                time.sleep(delay)


if __name__ == '__main__':
    try:
        send_heartbeat_data()
    except RuntimeError:
        print('Environment setup for script is incomplete.')
        print('Running dummy script instead...')
        time.sleep(0.5)
        fallback(delay=1)
