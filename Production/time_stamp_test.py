import datetime
import unittest

from time_stamp import TimeStamp

class TestTimeStamp(unittest.TestCase):
    def setUp(self):
        self.timestamp = TimeStamp()

    def datetime_map(self, datetime_obj):
        result = {}
        result['year'] = datetime_obj.year
        result['month'] = datetime_obj.month
        result['day'] = datetime_obj.day
        result['hour'] = datetime_obj.hour
        result['min'] = datetime_obj.minute
        result['sec'] = datetime_obj.second
        return result

    def test_default_timestamp(self):
        self.assertEqual(self.timestamp._tz, 'UTC')
        self.assertEqual(self.timestamp._timezones, {})
        self.timestamp._timezone_offsets()
        self.assertEqual(len(self.timestamp._timezones), 8)
        timestamp_dict = self.timestamp._create_timestamp()
        current_time = datetime.datetime.utcnow()
        current_time_map = self.datetime_map(current_time)
        for attr in current_time_map.keys():
            self.assertEqual(timestamp_dict[attr], current_time_map[attr])

    def test_non_UTC_timestamp(self):
        self.timestamp = TimeStamp('EST')
        self.assertEqual(self.timestamp._tz, 'EST')
        timestamp_dict = self.timestamp._create_timestamp()
        est_time = datetime.datetime.utcnow() - datetime.timedelta(hours=5)
        est_time_map = self.datetime_map(est_time)
        for attr in est_time_map.keys():
            self.assertEqual(timestamp_dict[attr], est_time_map[attr])

    def test_date(self):
        self.timestamp = TimeStamp('EST')
        full_timestamp = self.timestamp.timestamp()
        expected_day = full_timestamp.split()
        actual_day = self.timestamp.date()
        self.assertEqual(expected_day[0], actual_day)

    def test_time(self):
        self.timestamp = TimeStamp('EST')
        full_timestamp = self.timestamp.timestamp()
        expected_hour = full_timestamp.split()
        actual_hour = self.timestamp.time()
        self.assertEqual(expected_hour[1], actual_hour)


if __name__ == '__main__':
    unittest.main()
