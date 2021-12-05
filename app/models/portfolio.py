from .db import db
from sqlalchemy.orm import relationship


class Portfolio(db.Model):
  __tablename__ = "portfolios"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

  # a user has 1 portfolio
  user = db.relationship("User", back_populates="portfolios", uselist=False)
