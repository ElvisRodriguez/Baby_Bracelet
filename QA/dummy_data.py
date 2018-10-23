import datetime
import random

class DummyTime:
    def __init__(self, minutes):
        self.minutes = minutes

    def create_start_time(self):
        minutes = self.minutes
        values = {
            'days' : 0,
            'hours' : 0,
            'minutes' : 0
        }
        while minutes >= 60 * 24:
            values['days'] += 1
            minutes -= 60 * 24
        while minutes >= 60:
            values['hours'] += 1
            minutes -= 60
        values['minutes'] = minutes
        return datetime.timedelta(days=values['days'],
                                  hours=values['hours'],
                                  minutes=values['minutes'])

    def create_timestamp(self, date_obj):
        date = [date_obj.hour, date_obj.minute]
        if date[1] < 10:
            return '%i:0%i' % (date[0], date[1])
        else:
            return '%i:%i' % (date[0], date[1])


    def dummy_times(self):
        result = []
        min = self.minutes
        start_time = datetime.datetime.utcnow() - self.create_start_time()
        start_time -= datetime.timedelta(hours=4) # changes to EST timezone
        while min > 0:
            delta = datetime.timedelta(minutes=1)
            start_time += delta
            result.append(self.create_timestamp(start_time))
            min -= 1
        return result

class DummyHeartBeat:
    def __init__(self, heartbeats):
        self.heartbeats = heartbeats # matches amount of minutes from DummyTime

    def create_HB_list(self):
        result = []
        while self.heartbeats > 0:
            r = random.randint(80, 160)
            result.append(r)
            self.heartbeats -= 1
        return result
