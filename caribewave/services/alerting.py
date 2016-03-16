import time

from caribewave.alerting import Alert

def run(**kwargs):
    alert = Alert()
    while True:
        alert.call()
        time.sleep(10)
