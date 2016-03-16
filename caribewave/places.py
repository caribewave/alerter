import os
import requests
import json
import itertools

import settings
from utils import make_cache_dir
from sensors import Sensors


class Places(object):

    def __init__(self, sync=True):
        """
        Fetch the API to list the active sensors
        """
        self.places = []
        self.sensors = []
        self.synced = False
        if sync:
            self.sync()

    def sync(self):
        url = os.path.join(
            settings.PHEROMON_API_BASE,
            'allPlacesInfos'
        )
        resp = requests.get(url)
        if resp.status_code == 200:
            make_cache_dir()
            f = open(settings.PLACES_FILE, 'w')
            self.places = resp.json()
            self.sensors = list(itertools.chain(
                *[k["sensor_uids"] for k in self.places]))
            self.sensors = filter(lambda i: i is not None, self.sensors)
            f.write(json.dumps(self.places))
            f.close()
        self.synced = True

    def count_sensors(self):
        return len(self.sensors)
