from datetime import datetime

from .db import db


class TimestampedDocument(db.Document):
    meta = {"allow_inheritance": True, "abstract": True}

    created_at = db.DateTimeField(required=True, default=datetime.now)
    updated_at = db.DateTimeField(required=True, default=datetime.now)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)


class ConsumptionData(db.Document):
    main_engine_consumption = db.FloatField()
    aux_engine_consumption = db.FloatField()
    aux_boiler_consumption = db.FloatField()
    total_consumption = db.FloatField()


class Report(TimestampedDocument):
    report_number = db.IntField()
    report_from = db.DateTimeField()
    report_to = db.DateTimeField()
    consumption = db.ReferenceField(ConsumptionData)
