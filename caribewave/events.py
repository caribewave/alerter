import os
import json
from datetime import datetime

import settings


class EventsPersister(object):

    def __init__(self):
        self.events = []

    def add_events(self, events, sensor_uid, persist=True):
        for event in events:
            event["sensor"] = sensor_uid
            self.events.append(event)
        if persist:
            self.persist()

    def persist(self):
        files = {}
        for event in self.events:
            _dir =  os.path.join(
                settings.EVENTS_DIR,
                event["date"][0:10],
                event["date"][11:13]
            )
            filename = os.path.join(_dir, 'events.json')
            if not filename in files:
                if not os.path.exists(_dir):
                    os.makedirs(_dir)
                files[filename] = open(filename, 'wa')
            f = files[filename]
            f.write(json.dumps(event) + "\n")
        for _, f in files.iteritems():
            f.close()
        self.events = []


def list_events_dates():
    dates = []
    dirs = os.listdir(settings.EVENTS_DIR)
    for d in dirs:
        for hour in os.listdir(os.path.join(settings.EVENTS_DIR, d)):
            dates.append('/'.join((d, hour)))
    return sorted(dates)
