from flask.ext.api import FlaskAPI

import settings

app = FlaskAPI(__name__)


@app.route("/", methods=['GET'])
def home():
    return {"Welcome": "Welcome to the Caribewave API!"}


if __name__ == "__main__":
    app.run(debug=settings.DEBUG)
