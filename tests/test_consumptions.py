import json

import bson

from database.models import ConsumptionData
from tests.base_case import BaseCase


class TestConsumptionData(BaseCase):
    def setUp(self):
        super().setUp()
        self.payload = {
            "main_engine_consumption": 1410.20,
            "aux_engine_consumption": 2535.22,
            "aux_boiler_consumption": 3542.12,
            "total_consumption": 3333.55,
        }
        self.consumption_data = ConsumptionData(**self.payload).save()

    def test_consumption_create(self):
        # When
        response = self.app.post(
            "/api/consumptions",
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.payload),
        )

        # Then
        self.assertEqual(201, response.status_code)
        self.assertEqual(
            self.payload.get("main_engine_consumption"),
            response.json.get("main_engine_consumption"),
        )
        self.assertEqual(
            self.payload.get("aux_engine_consumption"),
            response.json.get("aux_engine_consumption"),
        )
        self.assertEqual(
            self.payload.get("aux_boiler_consumption"),
            response.json.get("aux_boiler_consumption"),
        )
        self.assertEqual(
            self.payload.get("total_consumption"),
            response.json.get("total_consumption"),
        )
        self.assertEqual(2, len(ConsumptionData.objects))

    def test_consumption_list(self):
        # When
        response = self.app.get(
            "/api/consumptions", headers={"Content-Type": "application/json"}
        )

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.json))

    def test_consumption_retrieve(self):
        # When
        id = self.consumption_data.id
        response = self.app.get(
            f"/api/consumption/{id}", headers={"Content-Type": "application/json"}
        )

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            self.payload.get("main_engine_consumption"),
            response.json.get("main_engine_consumption"),
        )
        self.assertEqual(
            self.payload.get("aux_engine_consumption"),
            response.json.get("aux_engine_consumption"),
        )
        self.assertEqual(
            self.payload.get("aux_boiler_consumption"),
            response.json.get("aux_boiler_consumption"),
        )
        self.assertEqual(
            self.payload.get("total_consumption"),
            response.json.get("total_consumption"),
        )

    def test_consumption_retrieve_wrong_id(self):
        # When
        id = bson.objectid.ObjectId()
        response = self.app.get(
            f"/api/consumption/{id}", headers={"Content-Type": "application/json"}
        )

        # Then
        self.assertEqual(400, response.status_code)

    def test_consumption_update(self):
        # Given
        payload = {
            "main_engine_consumption": 1111.11,
            "aux_engine_consumption": 2222.22,
            "aux_boiler_consumption": 3333.33,
            "total_consumption": 4444.44,
        }
        # When
        id = self.consumption_data.id
        response = self.app.put(
            f"/api/consumption/{id}",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
        )

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            payload.get("main_engine_consumption"),
            response.json.get("main_engine_consumption"),
        )
        self.assertEqual(
            payload.get("aux_engine_consumption"),
            response.json.get("aux_engine_consumption"),
        )
        self.assertEqual(
            payload.get("aux_boiler_consumption"),
            response.json.get("aux_boiler_consumption"),
        )
        self.assertEqual(
            payload.get("total_consumption"), response.json.get("total_consumption")
        )

    def test_consumption_delete(self):
        # When
        id = self.consumption_data.id
        response = self.app.delete(
            f"/api/consumption/{id}", headers={"Content-Type": "application/json"}
        )

        # Then
        self.assertEqual(204, response.status_code)
        self.assertEqual(0, len(ConsumptionData.objects))
