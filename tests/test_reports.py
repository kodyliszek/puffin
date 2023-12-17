import json

import bson

from database.models import Report, ConsumptionData
from tests.base_case import BaseCase


class TestReport(BaseCase):
    def setUp(self):
        super().setUp()
        self.consumption_data = ConsumptionData(
            main_engine_consumption=1410.20,
            aux_engine_consumption=2535.22,
            aux_boiler_consumption=542.12,
            total_consumption=3333.55,
        ).save()

        self.payload = {
            "report_number": 1,
            "report_from": "2024-05-15 12:03:05",
            "report_to": "2024-05-20 14:04:27",
            "consumption": str(self.consumption_data.id),
        }
        self.report = Report(**self.payload).save()

    def test_report_create(self):
        # When
        response = self.app.post(
            "/api/reports",
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.payload),
        )

        # Then
        self.assertEqual(201, response.status_code)
        self.assertEqual(2, len(Report.objects))

    def test_reports_list(self):
        # When
        response = self.app.get(
            "/api/reports", headers={"Content-Type": "application/json"}
        )

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.json))

    def test_report_retrieve(self):
        # When
        id = self.report.id
        response = self.app.get(
            f"/api/report/{id}", headers={"Content-Type": "application/json"}
        )

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(str(id), response.json.get("_id").get("$oid"))
        self.assertEqual(self.payload.get("report_number"), response.json.get("report_number"))

    def test_report_retrieve_wrong_id(self):
        # When
        id = bson.objectid.ObjectId()
        response = self.app.get(
            f"/api/report/{id}", headers={"Content-Type": "application/json"}
        )

        # Then
        self.assertEqual(400, response.status_code)


    def test_consumption_update(self):
        # Given
        payload = {
            "report_number": 2,
        }
        # When
        id = self.report.id
        response = self.app.put(
            f"/api/report/{id}",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
        )

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(str(id), response.json.get("_id").get("$oid"))
        self.assertEqual(payload.get("report_number"), response.json.get("report_number"))

    def test_report_delete(self):
        # When
        id = self.report.id
        response = self.app.delete(
            f"/api/report/{id}", headers={"Content-Type": "application/json"}
        )

        # Then
        self.assertEqual(204, response.status_code)
        self.assertEqual(0, len(Report.objects))
