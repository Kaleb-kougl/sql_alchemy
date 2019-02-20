import sqlite3
from db import db

# extend db.model, then tell it the table where they will be stored
class UserModel(db.Model):
    __tablename__ = "users"

    # tell it what columns it should contain
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    # ^ these are what are going to be saved to the db

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

