from .db import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Portfolio_Snap(db.Model):
  __tablename__ = "portfolio_snaps"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  value = db.Column(db.Float, nullable=False)
  portfolio_id = db.Column(db.Integer, db.ForeignKey("portfolios.id"), nullable=True)
  date = db.Column(db.DateTime(timezone=True), server_default=func.now())


  # 1 portfolio will have many snapshots
  portfolio = db.relationship("Portfolio", back_populates="portfolio_snaps", uselist=False)
