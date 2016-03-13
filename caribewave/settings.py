import os

ENV = os.getenv('CARIBEWAVE_ENV', 'sandbox')

MQTT_HOST = os.getenv('CARIBEWAVE_MQTT_HOST')
MQTT_PWD = os.getenv('CARIBEWAVE_MQTT_PWD')
MQTT_SENSORS_TOPIC = os.getenv(
    'CARIBEWAVE_MQTT_SENSORS_TOPIC',
    'measurement/#')

MQTT_HOST_DEBUG = "test.mosquitto.org"

DEBUG = ENV is not "prod"

CACHE_DIR = os.getenv('CARIBEWAVE_CACHE_DIR', '/tmp/caribewave')

PHEROMON_API_BASE = os.getenv(
    'CARIBEWAVE_PHEROMON_API_BASE')

PLACES_FILE = os.path.join(
    CACHE_DIR,
    'places.json'
)
