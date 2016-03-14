import os
import json

import settings


def make_cache_dir():
    dirs = [
        settings.CACHE_DIR,
        os.path.join(settings.CACHE_DIR, 'events'),
    ]

    for _dir in dirs:
        if not os.path.exists(_dir):
            os.makedirs(_dir)


def read(location):
    f = open(location)
    for line in f:
        yield line


def read_json_multiline(location):
    for entry in read(location):
        yield json.loads(entry)
