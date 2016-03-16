"""
Send fake data into test.mosquitto.org
"""
import time
import json
from datetime import datetime
import random
import paho.mqtt.client as mqtt

import settings


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(settings.MQTT_SENSORS_TOPIC_DEBUG)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def run(**kwargs):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(settings.MQTT_HOST_DEBUG, 1883, 60)

    while True:
        print "Send message"
        x = random.randint(1, 10000)
        y = random.randint(1, 10000)
        z = random.randint(1, 10000)
        msg = {
            "value": {
                "x": x,
                "y": y,
                "z": z
            },
            "date": datetime.now().isoformat()
        }
        time.sleep(1)
        client.publish(
            settings.MQTT_SENSORS_TOPIC_DEBUG,
            json.dumps([msg]))

if __name__ == "__main__":
    run()
