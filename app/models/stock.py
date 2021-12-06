from .db import db
from sqlalchemy.orm import relationship

class Stock(db.Model):
  __tablename__ = "stocks"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(30), nullable=False)
  ticker = db.Column(db.String(10), nullable=False, unique=True)
  about = db.Column(db.Text, nullable=False)
  ceo = db.Column(db.String(20), nullable=False)
  employee_count = db.Column(db.Integer, nullable=False)
  headquarters = db.Column(db.String(50), nullable=False)
  founded = db.Column(db.Integer, nullable=False)
  market_cap = db.Column(db.String, nullable=False)
  price_earnings_ratio = db.Column(db.Float, nullable=False)
  dividend_yield = db.Column(db.Float)
  average_volume = db.Column(db.String, nullable=False)
  high_today = db.Column(db.Float, nullable=False)
  low_today = db.Column(db.Float, nullable=False)
  open_price = db.Column(db.Float, nullable=False)
  volume = db.Column(db.String, nullable=False)
  week52_high = db.Column(db.Float, nullable=False)
  week52_low = db.Column(db.Float, nullable=False)
  news_id = db.Column(db.Integer, db.ForeignKey("news.id"), nullable=True)
  market_price = db.Column(db.Float, nullable=False)

  # watch list can have many stocks
  watchlists = db.relationship("WatchList", back_populates="stocks")

  # 1 fill can have 1 type of stock
  fill = db.relationship("Fill", back_populates="stock")

  # stock's price when fill 1 order
  # fill_order = db.relationship("Fill", back_populates="stock_price")
  