from .db import db

class News(db.Model):
  __tablename__ = "news"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  publisher = db.Column(db.String(30), nullable=False)
  title = db.Column(db.String(100), nullable=False)
  description = db.Column(db.Text, nullable=False)
  image_url = db.Column(db.String, nullable=False)
  date_published = db.Column(db.String, nullable=False)
