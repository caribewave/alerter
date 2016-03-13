import os
import requests
import json

import settings
from cache import make_cache_dir


class Places(object):

    def __init__(self, sync=True):
        """
        Fetch the API to list the active sensors
        """
        self.places = []
        self.sensor_uid_to_place = {}
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
            self._make_idx()
            f.write(json.dumps(self.places))
            f.close()

    def count_sensors(self):
        return sum(len(k['sensor_uids']) for k in self.places)

    def _make_idx(self):
        self.sensor_uid_to_place = {}
        for place in self.places:
            for uid in place["sensor_uids"]:
                self.sensor_uid_to_place[uid] = place
