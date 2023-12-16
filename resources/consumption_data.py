from flask import Response, request
from flask_restful import Resource

from database.models import ConsumptionData


class ConsumptionsDataApi(Resource):
    def get(self):
        consumption_data = ConsumptionData.objects().to_json()
        return Response(consumption_data, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        consumption_data = ConsumptionData(**body).save()
        return Response(consumption_data.to_json(), mimetype="application/json", status=201)


class ConsumptionDataApi(Resource):
    def put(self, id):
        body = request.get_json()
        ConsumptionData.objects.get(id=id).update(**body)
        consumption_data = ConsumptionData.objects.get(id=id)
        return Response(consumption_data.to_json(), mimetype="application/json", status=200)

    def delete(self, id):
        consumption_data = ConsumptionData.objects.get(id=id).delete()
        return Response("", mimetype="application/json", status=204)

    def get(self, id):
        consumption_data = ConsumptionData.objects.get(id=id)
        return Response(consumption_data.to_json(), mimetype="application/json", status=200)
