from .db import db

class Bank(db.Model):
  __tablename__ = "banks"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  bank_name = db.Column(db.String(20), nullable=False, unique=True)
