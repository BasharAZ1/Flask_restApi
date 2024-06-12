from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from enum import Enum
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username, phone, password, email):
        self._id = None
        self.username = username
        self.email=email
        self.phone = phone
        self.password_hash = generate_password_hash(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_id(self, _id):
        self._id = _id

    def get_id(self):
        return str(self._id)

class Package:
    def __init__(self, name, destination, price, duration, availability):
        self.name = name
        self.destination = destination
        self.price = price
        self.duration = duration
        self.availability = availability
        self.created_at = datetime.utcnow()


