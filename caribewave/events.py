import os
import json
from datetime import datetime, timedelta

import settings
import utils


class EventsPersister(object):

    def __init__(self):
        self.events = []
        self.files = {}

    def add_events(self, events, sensor_uid, persist=True):
        for event in events:
            event["sensor"] = sensor_uid
            self.events.append(event)
        if persist:
            self.persist()

    def persist(self):
        files = {}
        for event in self.events:
            filename = utils.get_events_file_location(event["date"])
            if filename not in files:
                files[filename] = open(filename, 'a')
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


def get_events(td=timedelta(minutes=10)):
    """
    :param td: Timedelta
    :type td : datetime.timedelta

    List events from `td` until now
    """
    date_end = datetime.utcnow()
    date_start = date_end - td
    print 'request files between {} and {}'.format(date_start, date_end)
    for date_hour in utils.date_hour_range(date_start, date_end):
        f = utils.get_events_file_location(date_hour.isoformat(), create_directory=False)
        if os.path.exists(f):
            for line in utils.read_json_multiline(f):
                d = utils.isodate_to_dt(line["date"])
                if d >= date_start:
                    yield line


def get_sensors_with_events(td=timedelta(minutes=10)):
    sensors = set()
    events = get_events(td)
    for event in events:
        sensors.add(event["sensor"])
    return list(sensors)
