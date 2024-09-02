"""This module defines a for user login"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """This a loginform object"""
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    keep_me = BooleanField("Keep me signed in")
    submit = SubmitField("SIGN IN")