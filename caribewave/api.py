import os
import json

from flask.ext.api import FlaskAPI

import settings
from events import list_events_dates


app = FlaskAPI(__name__)


@app.route("/", methods=['GET'])
def home():
    return {"Welcome": "Welcome to the Caribewave API!"}


@app.route("/places", methods=['GET'])
def places():
    if os.path.exists(settings.PLACES_FILE):
        f = open(settings.PLACES_FILE)
        return json.loads(f.read())
    return []


@app.route("/events/dates", methods=['GET'])
def events_dates():
    return list_events_dates()


if __name__ == "__main__":
    app.run(
        port=8080,
        debug=settings.DEBUG)
