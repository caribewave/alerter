import os
import json
import math
from datetime import datetime, timedelta

import settings


def make_cache_dir():
    dirs = [
        settings.CACHE_DIR,
        os.path.join(settings.CACHE_DIR, 'events'),
    ]

    for _dir in dirs:
        if not os.path.exists(_dir):
            os.makedirs(_dir)


def get_events_file_location(isodate, create_directory=True):
    _dir = os.path.join(
        settings.EVENTS_DIR,
        isodate[0:10],
        isodate[11:13]
    )
    if (create_directory and not
        os.path.exists(_dir)):
        print "Make dir", _dir
        os.makedirs(_dir)
    return os.path.join(_dir, 'events.json')
 

def read(location):
    f = open(location)
    for line in f:
        yield line


def read_json_multiline(location):
    for entry in read(location):
        yield json.loads(entry)


def date_range(start_date, end_date):
    """
    Return an iterator of dates from start_date to end_date (included)
    :type start_date: date
    :type end_date: date
    :rtype: collections.Iterable[date]
    """
    for n in range((end_date - start_date).days + 1):
        yield start_date + timedelta(n)


def date_hour_range(start_date, end_date):
    td = end_date - start_date
    hours = int(td.days * 24 + math.ceil(float(td.seconds) / 3600.0))
    for n in range(hours + 1):
        yield start_date + timedelta(hours=n)


def isodate_to_dt(isodate):
    return datetime.strptime(isodate, "%Y-%m-%dT%H:%M:%S.%fZ")
