from flask import Response, request
from flask_restful import Resource

from database.models import Report, ConsumptionData
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from resources.errors import SchemaValidationError, InternalServerError, ObjectNotExistsError


class ReportsApi(Resource):
    def get(self):
        """
        List all Reports
        ---
        tags:
          - Report
        responses:
          200:
            description: List all Reports
        """
        reports = Report.objects().to_json()
        return Response(reports, mimetype="application/json", status=200)

    def post(self):
        """
        Create a new Report
        ---
        tags:
          - Report
        parameters:
          - in: body
            name: body
            schema:
              id: Report
              properties:
                report_number:
                    type: number
                report_from:
                    type: string
                    pattern: '2020-06-12 12:24:36'
                report_to:
                    type: string
                    pattern: '2022-03-30 16:32:48'
                consumption:
                    type: string
        responses:
          201:
            description: Report created
        """
        try:
            body = request.get_json()
            ConsumptionData.objects.get(id=body.get("consumption"))
            report = Report(**body).save()
            return Response(report.to_json(), mimetype="application/json", status=201)
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except DoesNotExist:
            raise ObjectNotExistsError
        except Exception as e:
            raise InternalServerError


class ReportApi(Resource):
    def put(self, id):
        """
         Update a Report
         ---
         tags:
           - Report
         parameters:
           - in: path
             name: id
             type: string
           - in: body
             name: body
             schema:
               id: Report
               properties:
                 report_number:
                     type: number
                 report_from:
                     type: string
                     pattern: '2020-06-12 12:24:36'
                 report_to:
                     type: string
                     pattern: '2022-03-30 16:32:48'
                 consumption:
                     type: string
         responses:
           200:
             description: Report updated
         """
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
        """
        Delete Report
        ---
        tags:
          - Report
        parameters:
          - in: path
            name: id
            type: string
        responses:
          204:
            description: Report deleted
        """
        try:
            Report.objects.get(id=id).delete()
            return Response("", mimetype="application/json", status=204)
        except DoesNotExist:
            raise ObjectNotExistsError
        except Exception:
            raise InternalServerError
    
    def get(self, id):
        """
        Retrieve Report
        ---
        tags:
          - Report
        parameters:
          - in: path
            name: id
            type: string
        responses:
          200:
            description: Report retrieved
        """
        try:
            report = Report.objects.get(id=id)
            return Response(report.to_json(), mimetype="application/json", status=200)
        except DoesNotExist:
            raise ObjectNotExistsError
        except Exception:
            raise InternalServerError
