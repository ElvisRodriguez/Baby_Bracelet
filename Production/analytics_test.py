import random
import unittest

import analytics

class TestAnalyticMethods(unittest.TestCase):
    def setUp(self):
        self.average_hb = analytics.average_heartbeat
        self.is_rising = analytics.is_rising
        self.is_dropping = analytics.is_dropping
        self.hrv = analytics.heart_rate_variability
        self.data = None

    def test_average(self):
        self.data = [x * random.randint(2,10) for x in range(100)]
        average = sum(self.data) // len(self.data)
        self.assertEqual(average, self.average_hb(self.data))

    def test_is_rising_and_is_dropping(self):
        self.data = [x for x in range(100)]
        self.assertTrue(self.is_rising(self.data))
        self.assertFalse(self.is_dropping(self.data))
        self.data = [x for x in range(100, -1, -1)]
        self.assertTrue(self.is_dropping(self.data))
        self.assertFalse(self.is_rising(self.data))

    def test_rise_then_drop(self):
        self.data = [x for x in range(50)]
        self.data.extend([x for x in range(49,-1,-1)])
        self.assertTrue(self.is_rising(self.data))
        self.assertTrue(self.is_dropping(self.data))

    def test_HRV(self):
        HRV = self.hrv([x for x in range(0, 100, 1)])
        self.assertEqual(1, int(HRV))
        self.assertRaises(ZeroDivisionError, self.hrv,
                          interbeat_intervals=[x for x in range(1,100,100)])


if __name__ == '__main__':
    unittest.main()
