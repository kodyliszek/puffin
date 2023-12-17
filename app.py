from flask import Flask, jsonify
from flask_restful import Api
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from database.db import initialize_db
from resources.errors import errors
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app, errors=errors)


app.config.from_envvar('ENV_FILE_LOCATION')

db = initialize_db(app)
initialize_routes(api)


@app.route('/swagger')
def get_swagger():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)


# Swagger UI route
SWAGGER_URL = '/swagger-ui'
API_URL = '/swagger'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "My API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(debug=False)
