import argparse
import json

import paho.mqtt.client as mqtt
from caribewave import settings
from caribewave.events import EventsPersister


def get_sensor_uid_from_topic(topic):
    """
    topic_name is measurement/:sensor_uid/sismic
    """
    return topic.split('/')[1]


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    if userdata["debug"]:
        client.subscribe(settings.MQTT_SENSORS_TOPIC_DEBUG)
    else:
        client.subscribe(settings.MQTT_SENSORS_TOPIC)


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    sensor_uid = get_sensor_uid_from_topic(msg.topic)
    userdata["persister"].add_events(
        json.loads(msg.payload),
        sensor_uid=sensor_uid)


def run(debug=False):
    userdata = {
        "debug": debug,
        "persister": EventsPersister()
    }
    client = mqtt.Client(
        client_id="alerter_listener",
        userdata=userdata)

    if not debug:
        client.username_pw_set(username="pheroman", password=settings.MQTT_PWD)
    client.on_connect = on_connect
    client.on_message = on_message

    if debug:
        print "Connect to {}".format(settings.MQTT_HOST_DEBUG)
        client.connect(settings.MQTT_HOST_DEBUG, 1883, 60)
    else:
        print "Connect to {}".format(settings.MQTT_HOST)
        client.connect(settings.MQTT_HOST, 1883, 60)

    client.loop_forever()


def get_argparser():
    parser = argparse.ArgumentParser(description='Run listener')
    parser.add_argument('--debug', action='store_const',
                        const=True,
                        help='Pop data on test.mosquitto.org')
    return parser
