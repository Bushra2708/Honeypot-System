from app import db
from datetime import datetime

class Attack(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    ip_address = db.Column(db.String(100))

    username = db.Column(db.String(200))

    password = db.Column(db.String(200))

    browser = db.Column(db.String(200))

    operating_system = db.Column(db.String(200))

    device = db.Column(db.String(200))

    country = db.Column(db.String(200))

    city = db.Column(db.String(200))

    organization = db.Column(db.String(300))

    referrer = db.Column(db.Text)

    user_agent = db.Column(db.Text)

    def __repr__(self):

        return f"<Attack {self.ip_address}>"