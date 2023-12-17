from flask import Response, request
from flask_restful import Resource
from mongoengine.errors import (
    FieldDoesNotExist,
    DoesNotExist,
    ValidationError,
    InvalidQueryError,
)

from database.models import ConsumptionData
from resources.errors import (
    SchemaValidationError,
    InternalServerError,
    ObjectNotExistsError,
)


class ConsumptionsDataApi(Resource):
    def get(self):
        """
        List all ConsumptionData
        ---
        tags:
          - ConsumptionData
        responses:
          200:
            description: List all ConsumptionData
        """
        consumption_data = ConsumptionData.objects().to_json()
        return Response(consumption_data, mimetype="application/json", status=200)

    def post(self):
        """
        Create a new ConsumptionData
        ---
        tags:
          - ConsumptionData
        parameters:
          - in: body
            name: body
            schema:
              id: ConsumptionData
              properties:
                main_engine_consumption:
                    type: number
                aux_engine_consumption:
                    type: number
                aux_boiler_consumption:
                    type: number
                total_consumption:
                    type: number
        responses:
          201:
            description: ConsumptionData created
        """
        try:
            body = request.get_json()
            consumption_data = ConsumptionData(**body).save()
            return Response(
                consumption_data.to_json(), mimetype="application/json", status=201
            )
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception:
            raise InternalServerError


class ConsumptionDataApi(Resource):
    def put(self, id):
        """
        Update ConsumptionData
        ---
        tags:
          - ConsumptionData
        parameters:
          - in: path
            name: id
            type: string
          - in: body
            name: body
            schema:
              id: ConsumptionData
              properties:
                main_engine_consumption:
                    type: number
                aux_engine_consumption:
                    type: number
                aux_boiler_consumption:
                    type: number
                total_consumption:
                    type: number
        responses:
          200:
            description: ConsumptionData updated
        """
        try:
            body = request.get_json()
            ConsumptionData.objects.get(id=id).update(**body)
            consumption_data = ConsumptionData.objects.get(id=id)
            return Response(
                consumption_data.to_json(), mimetype="application/json", status=200
            )
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise ObjectNotExistsError
        except Exception as e:
            raise InternalServerError

    def delete(self, id):
        """
        Delete ConsumptionData
        ---
        tags:
          - ConsumptionData
        parameters:
          - in: path
            name: id
            type: string
        responses:
          204:
            description: ConsumptionData deleted
        """
        try:
            ConsumptionData.objects.get(id=id).delete()
            return Response("", mimetype="application/json", status=204)
        except DoesNotExist:
            raise ObjectNotExistsError
        except Exception:
            raise InternalServerError

    def get(self, id):
        """
        Retrieve ConsumptionData
        ---
        tags:
          - ConsumptionData
        parameters:
          - in: path
            name: id
            type: string
        responses:
          200:
            description: ConsumptionData retrieved
        """
        try:
            consumption_data = ConsumptionData.objects.get(id=id)
            return Response(
                consumption_data.to_json(), mimetype="application/json", status=200
            )
        except DoesNotExist:
            raise ObjectNotExistsError
        except Exception:
            raise InternalServerError
