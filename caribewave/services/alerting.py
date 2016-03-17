import time

from caribewave.alerting import Alert


def run(**kwargs):
    alert = Alert()
    while True:
        has_alert = alert.call()
        if has_alert:
            print 'Alert sent, sleep 60 secondes'
            time.sleep(60)
        else:
            print "Sleep 3 secondes"
            time.sleep(3)
