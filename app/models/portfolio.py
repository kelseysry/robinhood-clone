from .db import db
from sqlalchemy.orm import relationship


class Portfolio(db.Model):
  __tablename__ = "portfolios"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
  buying_power = db.Column(db.Float)
  bank_id = db.Column(db.Integer, db.ForeignKey("banks.id"), nullable=True)

  # a user has 1 portfolio
  user = db.relationship("User", back_populates="portfolios", uselist=False)

  # 1 portfolio can have many fills
  fills = db.relationship("Fill", back_populates="portfolio")

  # 1 portfolio will have many snapshots
  portfolio_snaps = db.relationship("Portfolio_Snap", back_populates="portfolio")

  #one user/portfolio can have many bank accounts
  bank = db.relationship("Bank", back_populates="portfolio")
