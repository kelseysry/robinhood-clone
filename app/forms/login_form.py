from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User

# custom validator
# validation for LoginForm below
def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if not user:
        raise ValidationError('Email provided not found.')

# validation for LoginForm below
def password_matches(form, field):
    # Checking if password matches
    password = field.data
    email = form.data['email']
    user = User.query.filter(User.email == email).first()
    if not user:
        raise ValidationError('No such user exists.')
    if not user.check_password(password):
        raise ValidationError('Password was incorrect.')

# not form for display. So that's why don't see submit button
# This is just to validate info on the backend. We'll be using a react form that
# will pass info as JSON obj to backend sign_up view function in api/auth_routes.py
# after click react submit button which sends a post request.
# wtforms will pair react fields to the flaskform field names.
class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), user_exists])
    password = StringField('password', validators=[
                           DataRequired(), password_matches])
