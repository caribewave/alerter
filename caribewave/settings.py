import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOP_DIR = '/'.join(BASE_DIR.split('/')[0:-1])
if TOP_DIR not in sys.path:
    sys.path.append(TOP_DIR)

ENV = os.getenv('CARIBEWAVE_ENV', 'sandbox')

MQTT_HOST = os.getenv('CARIBEWAVE_MQTT_HOST')
MQTT_PWD = os.getenv('CARIBEWAVE_MQTT_PWD')
MQTT_SENSORS_TOPIC = os.getenv(
    'CARIBEWAVE_MQTT_SENSORS_TOPIC',
    'measurement/#')

MQTT_HOST_DEBUG = "test.mosquitto.org"
MQTT_SENSORS_TOPIC_DEBUG = "measurement/sender"

DEBUG = ENV is not "prod"

CACHE_DIR = os.getenv('CARIBEWAVE_CACHE_DIR', '/tmp/caribewave')

PHEROMON_API_BASE = os.getenv(
    'CARIBEWAVE_PHEROMON_API_BASE')

PLACES_FILE = os.path.join(
    CACHE_DIR,
    'places.json'
)

EVENTS_DIR = os.path.join(
    CACHE_DIR,
    'events'
)
