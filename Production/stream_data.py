import random
import requests
import time

#import heartBeats


URL = 'https://elvisrodriguez.pythonanywhere.com/data'

def gen_fake_hb():
    val = random.randint(90,110)
    while True:
        yield val

if __name__ == '__main__':
    while True:
        fake_hb = gen_fake_hb()
        heart_rate = next(fake_hb)
        payload = {'heartbeat':str(heart_rate)}
        r = requests.get(URL)
        print('STATUS CODE: ', r.status_code)
        r = requests.post(URL, data=payload)
        print('SENT HEART RATE OF: ', heart_rate)
        time.sleep(1)
