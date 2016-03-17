import os
import sys
import json

ENV = None


def set_conf(filename):
    mod = sys.modules[__name__]
    json_conf = json.load(open(filename))
    for k, v in json_conf.iteritems():
        setattr(mod, k, v)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOP_DIR = '/'.join(BASE_DIR.split('/')[0:-1])
if TOP_DIR not in sys.path:
    sys.path.append(TOP_DIR)

JSON_FILE = os.path.join(
    TOP_DIR,
    'conf',
    'config.json'
)

if os.path.exists(JSON_FILE):
    set_conf(JSON_FILE)
else:
    raise Exception('config.json does not exists')

MQTT_SENSORS_TOPIC = "measurement/#"
MQTT_HOST_DEBUG = "test.mosquitto.org"
MQTT_SENSORS_TOPIC_DEBUG = "measurement/sender"

DEBUG = ENV is not "prod"
