from flask import Response, request
from flask_restful import Resource

from database.models import Report, ConsumptionData


class ReportsApi(Resource):
    def get(self):
        reports = Report.objects().to_json()
        return Response(reports, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        report = Report(**body).save()
        return Response(report.to_json(), mimetype="application/json", status=201)


class ReportApi(Resource):
    def put(self, id):
        body = request.get_json()
        consumption = ConsumptionData.objects.get(id=body.get("consumption"))
        body["consumption"] = consumption
        Report.objects.get(id=id).update(**body)
        report = Report.objects.get(id=id)
        return Response(report.to_json(), mimetype="application/json", status=200)

    def delete(self, id):
        report = Report.objects.get(id=id).delete()
        return Response("", mimetype="application/json", status=204)

    def get(self, id):
        report = Report.objects.get(id=id)
        return Response(report.to_json(), mimetype="application/json", status=200)
