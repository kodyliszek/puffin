from flask import Response, request
from flask_restful import Resource

from database.models import ConsumptionData
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from resources.errors import SchemaValidationError,InternalServerError, ObjectNotExistsError

class ConsumptionsDataApi(Resource):
    def get(self):
        consumption_data = ConsumptionData.objects().to_json()
        return Response(consumption_data, mimetype="application/json", status=200)

    def post(self):
        try:
            body = request.get_json()
            consumption_data = ConsumptionData(**body).save()
            return Response(consumption_data.to_json(), mimetype="application/json", status=201)
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception:
            raise InternalServerError


class ConsumptionDataApi(Resource):
    def put(self, id):
        try:
            body = request.get_json()
            ConsumptionData.objects.get(id=id).update(**body)
            consumption_data = ConsumptionData.objects.get(id=id)
            return Response(consumption_data.to_json(), mimetype="application/json", status=200)
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise ObjectNotExistsError
        except Exception:
            raise InternalServerError

    def delete(self, id):
        try:
            ConsumptionData.objects.get(id=id).delete()
            return Response("", mimetype="application/json", status=204)
        except DoesNotExist:
            raise ObjectNotExistsError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            consumption_data = ConsumptionData.objects.get(id=id)
            return Response(consumption_data.to_json(), mimetype="application/json", status=200)
        except DoesNotExist:
            raise ObjectNotExistsError
        except Exception:
            raise InternalServerError
