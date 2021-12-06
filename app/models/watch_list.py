from .db import db


class WatchList(db.Model):
  __tablename__ = "watchlists"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
  stock_id = db.Column(db.Integer, db.ForeignKey("stocks.id"))

  # a user has 1 watchlist
  user = db.relationship("User", back_populates="watchlist", uselist=False)

  # watch list can have many stocks
  stocks = db.relationship("Stock", back_populates="watchlists")
