"""
Send fake data into test.mosquitto.org
"""
import json
import time
import random
import paho.mqtt.client as mqtt

import settings


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(settings.MQTT_SENSORS_TOPIC)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def run():
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
            "sensor": "mariegalante-01",
            "ts": int(time.time()),
            "x": x,
            "y": y,
            "z": z}
        client.publish(settings.MQTT_SENSORS_TOPIC, json.dumps(msg))
        time.sleep(1)

if __name__ == "__main__":
    run()
