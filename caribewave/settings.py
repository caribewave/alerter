import os

ENV = os.getenv('CARIBEWAVE_ENV', 'sandbox')
MQTT_HOST = os.getenv('MQTT_HOST', 'test.mosquitto.org')

DEBUG = ENV is not "prod"
