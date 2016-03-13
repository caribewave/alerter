import time
import json
import argparse

import paho.mqtt.client as mqtt
import settings


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(settings.MQTT_SENSORS_TOPIC)


def on_message(client, userdata, msg):
    #row = json.loads(msg.payload)
    #row["ts_received"] = int(time.time())
    # TODO : Store data
    print(msg.topic+" "+str(msg.payload))


def run(debug=True):
    client = mqtt.Client(userdata={})
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
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run listener')
    parser.add_argument('--debug', action='store_const',
                        const=True,
                        help='Environment (sandbox/prod)')
    args = parser.parse_args()
    run(args.debug)
