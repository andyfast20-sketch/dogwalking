from datetime import datetime

from . import db


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    pet_name = db.Column(db.String(120), nullable=False)
    service_type = db.Column(db.String(80), nullable=False)
    scheduled_for = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:  # pragma: no cover - string formatting only
        return f"<Booking {self.client_name} - {self.service_type}>"
