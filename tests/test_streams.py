import random
import time
import unittest
import mock

from caribewave.streams import SensorsStream


def make_random_entry(sensor="mariegalante-01"):
    x = random.randint(1, 10000)
    y = random.randint(1, 10000)
    z = random.randint(1, 10000)
    return {
        "sensor": "mariegalante-01",
        "ts": int(time.time()),
        "x": x,
        "y": y,
        "z": z}


class SensorsStreamTest(unittest.TestCase):

    def setUp(self):
        stream = SensorsStream()
        stream.add(make_random_entry())
        stream.add(make_random_entry())
        stream.add(make_random_entry())
        self.stream = stream

    @mock.patch('caribewave.streams.count_active_sensors')
    def test_alert_true(self, mock_count_active_sensors):
        mock_count_active_sensors.return_value = 1
        self.assertTrue(self.stream.alert())

    @mock.patch('caribewave.streams.count_active_sensors')
    def test_alert_false(self, mock_count_active_sensors):
        mock_count_active_sensors.return_value = 2
        self.assertFalse(self.stream.alert())
