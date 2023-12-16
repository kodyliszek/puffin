import os

from flask import Flask

from database.db import initialize_db

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
