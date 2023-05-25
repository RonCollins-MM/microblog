#!/usr/bin/env python3

"""Module that contains the Forms for microblog app"""

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """Form for User login to microblog web app"""

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')