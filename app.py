import os

from flask import Flask
from flask_restful import Api

from database.db import initialize_db
from resources.routes import initialize_routes
from resources.errors import errors

app = Flask(__name__)
api = Api(app, errors=errors)

app.config.from_envvar('ENV_FILE_LOCATION')

db = initialize_db(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run(debug=True)
