import time

from caribewave.alerting import Alert

def run():
    alert = Alert()
    while True:
        alert.call()
        time.sleep(10)
