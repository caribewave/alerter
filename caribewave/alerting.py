import json
from datetime import datetime, timedelta

from caribewave.places import Places
from caribewave.sensors import Sensors
from caribewave.events import get_sensors_with_events
from caribewave import sns


class Alert(object):

    def __init__(self):
        self.places = Places()
        self.sensors = Sensors()
        self.last_alert = None

    def call(self):
        """
        Return True if an event has been sent
        """

        self.places.sync()

        alive_sensors = self.sensors.check(self.places.sensors)
        print "Alive sensors", alive_sensors

        events_sensors = get_sensors_with_events(
            td=timedelta(seconds=50))
        print "Sensors with events", events_sensors

        if alive_sensors and sorted(alive_sensors) == sorted(events_sensors):
            self.last_alert = datetime.utcnow()
            self.prevent(events_sensors)
            return True
        return False

    def prevent(self, sensor_uids):
        print "All sensors active, send to SNS and MQTT"
        msg = "Seismic activity detected. Please find shelter promptly"
        sns.send_message(msg)
        payload = {
            "message": msg,
            "sensors_uids": sensor_uids
        }
        self.sensors.client.publish(
            'alert/general',
            json.dumps(payload)
        )
