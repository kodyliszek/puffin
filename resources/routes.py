from resources.consumption_data import ConsumptionDataApi, ConsumptionsDataApi
from resources.report import ReportApi, ReportsApi


def initialize_routes(api):
    api.add_resource(ReportsApi, "/api/reports")
    api.add_resource(ReportApi, "/api/report/<id>")

    api.add_resource(ConsumptionsDataApi, "/api/consumptions")
    api.add_resource(ConsumptionDataApi, "/api/consumption/<id>")
