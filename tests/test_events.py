import os
import random
import time
import unittest
import json
import shutil
from datetime import datetime

from caribewave import settings
from caribewave.events import EventsPersister
from caribewave import settings
from caribewave.utils import read_json_multiline


def make_random_entry(hour=1, sensor="mariegalante-01"):
    x = random.randint(1, 10000)
    y = random.randint(1, 10000)
    z = random.randint(1, 10000)
    return {
        "sensor": sensor,
        "value": {
            "x": x,
            "y": y,
            "z": z
        },
        "date": datetime(2016, 3, 11, hour, 1).isoformat()
    }


def make_random_entries(nb, hour=1, sensor="mariegalante-01"):
    entries = []
    for i in xrange(0, nb):
        entries.append(make_random_entry(hour, sensor))
    return entries


class AlertingTest(unittest.TestCase):
    def setUp(self):
        settings.CACHE_DIR = '/tmp/caribewave_tests/'

    def tearDown(self):
        shutil.rmtree(settings.CACHE_DIR)

    def test_persist(self):
        ep = EventsPersister()
        events = []
        events.append(make_random_entries(10, hour=1))
        events.append(make_random_entries(10, hour=2))
        ep.add_events(events[0] + events[1], sensor_uid="mariegalante-01")
        for hour in (1, 2):
            filename = os.path.join(
                settings.CACHE_DIR,
                'events',
                '2016-03-11',
                str(hour).zfill(2),
                'events.json')
            self.assertTrue(
                os.path.exists(filename))
            self.assertEquals(
                events[hour - 1],
                list(read_json_multiline(filename)))
