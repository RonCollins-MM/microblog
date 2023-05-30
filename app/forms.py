#!/usr/bin/env python3

"""Module that contains the Forms for microblog app"""

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    """Form for User login to microblog web app"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

class RegistrationForm(FlaskForm):
    """Form for User registration to the microblog web app"""

    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password',
                              validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """Ensure username is not already in use"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already in use !')

    def validate_email(self, email):
        """Ensure email is unique in database"""
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('User with that email already exists !!')