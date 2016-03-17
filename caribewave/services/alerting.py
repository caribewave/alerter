import time
from datetime import datetime, timedelta

from caribewave.alerting import Alert

def run(**kwargs):
    alert = Alert()
    while True:
        has_alert = alert.call()
        if has_alert:
            print 'Alert sent, sleep 3 minutes'
            time.sleep(180)
        else:
            print "Sleep 3 secondes"
            time.sleep(3)
