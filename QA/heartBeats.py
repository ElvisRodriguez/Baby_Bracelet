# Simple heart beat reader for Raspberry pi using ADS1x15 family of ADCs and a pulse sensor - http://pulsesensor.com/.
# The code borrows heavily from Tony DiCola's examples of using ADS1x15 with
# Raspberry pi and WorldFamousElectronics's code for PULSESensor_Amped_Arduino

# Author: Udayan Kumar
# License: Public Domain

# Modified By: @Atawear Team

import time

import Adafruit_ADS1x15

# Globals
ADC = Adafruit_ADS1x15.ADS1015()
GAIN = 2/3
CURRENT_STATE = 0
THRESHOLD = 525  # mid point in the waveform
PEAK = 512
TROUGTROUGH = 512
TIME_IN_MILLISECS = 0
TIME_OF_LAST_HEARTBEAT = 0
FIRST_HEARTBEAT = True
SECOND_HEARTBEAT = False
PULSE = False
INTER_BEAT_INTERVAL = 600
RATE = [0]*10
AMPLITUDE = 100
LAST_TIME = int(time.time()*1000)


if __name__ == '__main__':
    while True:
        Signal = ADC.read_adc(0, gain=GAIN)   #TODO: Select the correct ADC channel. A0 currently selected
        CURRENT_TIME = int(time.time()*1000)

        TIME_IN_MILLISECS += CURRENT_TIME - LAST_TIME
        LAST_TIME = CURRENT_TIME
        TIME_SINCE_LAST_HEARTBEAT = TIME_IN_MILLISECS - TIME_OF_LAST_HEARTBEAT

        if Signal < THRESHOLD and TIME_SINCE_LAST_HEARTBEAT > (INTER_BEAT_INTERVAL/5.0)*3.0: # avoid dichrotic noise by waiting 3/5 of last INTER_BEAT_INTERVAL
            if Signal < TROUGH:
              TROUGH = Signal # keep track of lowest point in pulse wave

        if Signal > THRESHOLD and  Signal > PEAK: # THRESHOLD condition helps avoid noise
            PEAK = Signal # keep track of highest point in pulse wave

        # signal surges up in value every time there is a pulse
        if TIME_SINCE_LAST_HEARTBEAT > 250: # avoid high frequency noise
            if (Signal > THRESHOLD) and (PULSE == False) and (TIME_SINCE_LAST_HEARTBEAT > INTER_BEAT_INTERVAL/5*3):
              PULSE = True
              INTER_BEAT_INTERVAL = TIME_IN_MILLISECS - TIME_OF_LAST_HEARTBEAT
              TIME_OF_LAST_HEARTBEAT = TIME_IN_MILLISECS

              if SECOND_HEARTBEAT:
                SECOND_HEARTBEAT = False
                for i in range(0,10): # seed the running total to get a realisitic BPM at startup
                  RATE[i] = INTER_BEAT_INTERVAL

              if FIRST_HEARTBEAT:
                FIRST_HEARTBEAT = False
                SECOND_HEARTBEAT = True
                continue # INTER_BEAT_INTERVAL value is unreliable so discard it


              # keep a running total of the last 10 INTER_BEAT_INTERVAL values
              runningTotal = 0

              for i in range(0,9):
                RATE[i] = RATE[i+1]
                runningTotal += RATE[i]

              RATE[9] = INTER_BEAT_INTERVAL
              runningTotal += RATE[9]
              runningTotal //= 10
              BPM = 60000//runningTotal
              print('BPM: {}'.format(BPM))

        if Signal < THRESHOLD and PULSE == True: # when the values are going down, the beat is over
            PULSE = False
            AMPLITUDE = PEAK - TROUGH
            THRESHOLD = AMPLITUDE//2 + TROUGH
            PEAK = THRESHOLD
            TROUGH = THRESHOLD

        if TIME_SINCE_LAST_HEARTBEAT > 2500:
            THRESHOLD = 512
            PEAK = 512
            TROUGH = 512
            TIME_OF_LAST_HEARTBEAT = TIME_IN_MILLISECS
            FIRST_HEARTBEAT = True
            SECOND_HEARTBEAT = False
            print("no beats found")

        time.sleep(0.005)
