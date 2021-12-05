from .db import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Fill(db.Model):
  __tablename__ = "fills"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  portfolio_id = db.Column(db.Integer, db.ForeignKey("portfolios.id"), nullable=True)
  stock_id = db.Column(db.Integer, db.ForeignKey("stocks.id"), nullable=True)
  shares = db.Column(db.Integer, nullable=False)
  purchase_date = db.Column(db.DateTime(timezone=True), server_default=func.now())


  # 1 portfolio can have many fills
  portfolio = db.relationship("Portfolio", back_populates="fills")

  # 1 fill can have 1 type of stock.
  stock = db.relationship("Stock", back_populates="fill", uselist=False)

  # # stock's price when fill 1 order
  # stock_price = db.relationship("Stock", back_populates="fill_order", uselist=False)
