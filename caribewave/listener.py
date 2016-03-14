import argparse
import json

import paho.mqtt.client as mqtt
import settings
from events import EventsPersister


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
    sensor_uid = get_sensor_uid_from_topic(msg.topic)
    userdata["persister"].add_events(
        json.loads(msg.payload),
        sensor_uid=sensor_uid)
    print(msg.topic+" "+str(msg.payload))


def run(debug=True):
    userdata = {
        "debug": debug,
        "persister": EventsPersister()
    }
    client = mqtt.Client(userdata=userdata)

    if not debug:
        client.username_pw_set(username="listener", password=settings.MQTT_PWD)
    client.on_connect = on_connect
    client.on_message = on_message

    if debug:
        print "Connect to {}".format(settings.MQTT_HOST_DEBUG)
        client.connect(settings.MQTT_HOST_DEBUG, 1883, 60)
    else:
        print "Connect to {}".format(settings.MQTT_HOST)
        client.connect(settings.MQTT_HOST, 1883, 60)
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available
    # that give a threaded interface and a
    # manual interface.
    client.loop_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run listener')
    parser.add_argument('--debug', action='store_const',
                        const=True,
                        help='Pop data on test.mosquitto.org')
    args = parser.parse_args()
    run(args.debug)
