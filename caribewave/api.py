import os
import json

from flask.ext.api import FlaskAPI

import settings

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


if __name__ == "__main__":
    app.run(debug=settings.DEBUG)
