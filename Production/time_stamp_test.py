import datetime
import unittest

from time_stamp import TimeStamp

class TestTimeStamp(unittest.TestCase):
    def setUp(self):
        self.timestamp = TimeStamp()

    def test_default_timestamp(self):
        self.assertEqual(self.timestamp._tz, 'UTC')
        self.assertEqual(self.timestamp._timezones, {})
        self.timestamp._timezone_offsets()
        self.assertEqual(len(self.timestamp._timezones), 8)

    def test_non_UTC_timestamp(self):
        self.timestamp = TimeStamp('EST')
        self.assertEqual(self.timestamp._tz, 'EST')
        timestamp_dict = self.timestamp._create_timestamp()
        current_hour = datetime.datetime.utcnow().hour
        self.assertNotEqual(timestamp_dict['hour'], current_hour)

    def test_current_day(self):
        self.timestamp = TimeStamp('EST')
        full_timestamp = self.timestamp.full_timestamp()
        expected_day = full_timestamp.split()
        actual_day = self.timestamp.current_day()
        self.assertEqual(expected_day[0], actual_day)

    def test_current_hour(self):
        self.timestamp = TimeStamp('EST')
        full_timestamp = self.timestamp.full_timestamp()
        expected_hour = full_timestamp.split()
        actual_hour = self.timestamp.current_hour()
        self.assertEqual(expected_hour[1], actual_hour)

if __name__ == '__main__':
    unittest.main()
