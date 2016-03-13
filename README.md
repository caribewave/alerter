# Caribewave Alerter

Listen to sensors data and publish to an alert topic when situation is critical.


## Installation

```sh
export CARIBEWAVE_ENV=sandbox  # Or prod
export MQTT_HOST=mqtt.host.com
virtualenv venv
source venv/bin/activate
./script/setup
```

## Running listener

```
python caribewave/listener.py
```


## Sending fake data

```
python caribewave/sender.py
```
