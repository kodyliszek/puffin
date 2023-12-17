from flask import Response, request
from flask_restful import Resource

from database.models import Report, ConsumptionData
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from resources.errors import SchemaValidationError, InternalServerError, ObjectNotExistsError


class ReportsApi(Resource):
    def get(self):
        reports = Report.objects().to_json()
        return Response(reports, mimetype="application/json", status=200)

    def post(self):
        try:
            body = request.get_json()
            report = Report(**body).save()
            return Response(report.to_json(), mimetype="application/json", status=201)
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError


class ReportApi(Resource):
    def put(self, id):
        try:
            report = Report.objects.get(id=id)
            body = request.get_json()
            consumption_id = body.get("consumption") or report.consumption.id
            consumption = ConsumptionData.objects.get(id=consumption_id)
            body["consumption"] = consumption
            Report.objects.get(id=id).update(**body)
            report = Report.objects.get(id=id)
            return Response(report.to_json(), mimetype="application/json", status=200)
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise ObjectNotExistsError
        except Exception:
            raise InternalServerError
        
    def delete(self, id):
        try:
            Report.objects.get(id=id).delete()
            return Response("", mimetype="application/json", status=204)
        except DoesNotExist:
            raise ObjectNotExistsError
        except Exception:
            raise InternalServerError
    
    def get(self, id):
        try:
            report = Report.objects.get(id=id)
            return Response(report.to_json(), mimetype="application/json", status=200)
        except DoesNotExist:
            raise ObjectNotExistsError
        except Exception:
            raise InternalServerError
