import json
import time
import random
import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("presence")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
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
    client.publish("caribewave", json.dumps(msg))
    time.sleep(1)
