import os

ENV = os.getenv('CARIBEWAVE_ENV', 'sandbox')

MQTT_HOST = os.getenv('CARIBEWAVE_MQTT_HOST')
MQTT_PWD = os.getenv('CARIBEWAVE_MQTT_PWD')
MQTT_SENSORS_TOPIC = os.getenv(
    'CARIBEWAVE_MQTT_SENSORS_TOPIC',
    'measurement/#')

MQTT_HOST_DEBUG = "test.mosquitto.org"

DEBUG = ENV is not "prod"
