from caribewave.sensors import count_active_sensors


class SensorsStream(object):

    def __init__(self):
        self.data = []

    def add(self, entry):
        self.data.append(entry)

    def clean(self):
        """
        Clean data recorded for more than 1 hour
        """
        pass

    def alert(self):
        """
        Return `True` if all sensors are active
        Check if an alert should be sent
        """
        return (len(set(entry["sensor"] for entry in self.data)) ==
                count_active_sensors())
