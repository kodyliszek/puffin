import os

from flask import Flask
from flask_restful import Api

from database.db import initialize_db
from resources.routes import initialize_routes
from resources.errors import errors

app = Flask(__name__)
api = Api(app, errors=errors)

DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_URL = f'mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

app.config['MONGODB_SETTINGS'] = {
    'host': DB_URL
}

db = initialize_db(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run(debug=True)
