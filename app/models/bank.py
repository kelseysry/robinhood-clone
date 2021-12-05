from .db import db
from sqlalchemy.orm import relationship


class Bank(db.Model):
  __tablename__ = "banks"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  bank_name = db.Column(db.String(20), nullable=False, unique=True)

  # 1 bank can have many users
  users = db.relationship("User", back_populates="bank")
