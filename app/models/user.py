from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# UserMixin allows us to use user auth on user model
# werkzeug.security  debugger and hash password

# create py file for each model in db
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    buying_power = db.Column(db.Float)
    bank_id = db.Column(db.Integer, primary_key=True)

    @property
    def password(self): # getter
        return self.hashed_password

    @password.setter # setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

# used in app/forms/login_form to check password when logging in against db
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
