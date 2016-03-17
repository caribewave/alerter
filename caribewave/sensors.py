import json
import paho.mqtt.client as mqtt
import time

import settings


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe('cmdResult/#')


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    sensor_id = msg.topic.split('/')[1]
    if json.loads(msg.payload)["result"] == "OK":
        userdata[sensor_id] = True


class Sensors(object):

    def __init__(self):
        self.client = mqtt.Client(client_id="alerter_status")
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.username_pw_set(
            username="pheroman",
            password=settings.MQTT_PWD)
        print "Connect to {}".format(settings.MQTT_HOST)
        self.client.connect(settings.MQTT_HOST, 1883, 60)

    def check(self, sensor_ids):
        """
        Check if `sensor_id` is active
        """
        userdata = {
            sensor_id: False
            for sensor_id in sensor_ids
        }

        self.client.user_data_set(userdata)
        for sensor_id in sensor_ids:
            print "Publish to {}".format(sensor_id)
            self.client.publish(sensor_id, 'status', qos=0)
        self.client.loop_start()
        time.sleep(3)
        self.client.loop_stop(force=False)
        return [k for k, v in userdata.iteritems() if v is True]
