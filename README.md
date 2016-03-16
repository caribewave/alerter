# Caribewave Alerter

Listen to sensors data and publish to an alert topic when situation is critical.


## Installation

```sh
export CARIBEWAVE_DIR=/my/dir
export CARIBEWAVE_MQTT_HOST=127.0.0.1
export CARIBEWAVE_MQTT_PWD=mypwd
export CARIBEWAVE_MQTT_SENSORS_TOPIC=measurement/#
export CARIBEWAVE_PHEROMON_API_BASE=https://caribe.ants.builders/
export AWS_REGION=us-west-2  # Oregon
export SNS_APP_ID=arn:aws:sns:xxx:yyy
export SNS_ALERT_TOPIC=arn:aws:sns:us-west-2:xxx:yyy:alerts

virtualenv venv
source venv/bin/activate
./script/setup
```

## Running listener

Service recording all sensors events into static files.

Events are splited into files by day + hour

```
python caribewave/runservice.py listener
```

## Running alerting service

Alerting service regularly (minute) checks all active sensors.
If all active sensors sent at least one event in the 10 last minutes,
SNS and MQTT messages are sent.

```
python caribewave/runservice.py alerting
```

## Running API

The main purpose of the API is to register application tokens for SNS and Google Cloud Messaging registrations.
We may propose more endpoints later.

```
python caribewave/api.py
```

Service is available on http://127.0.0.1:8080


## Sending fake data

```
python caribewave/runservice.py sender
```
