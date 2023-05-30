#!/usr/bin/env python3

"""Contains model classes for the blog app"""

from app import db, login
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    """Represents users of the blog app"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        """Internal representation of objects of this class"""

        return f'[User] (username={self.username} email={self.email})'

    def set_password(self, password):
        """Hashes password and stores the hash generated in the object"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the password entered against the hash stored in the object

        Returns
        -------
        boolean - True if matche, False otherwise
        """
        return check_password_hash(self.password_hash,password)

@login.user_loader
def load_user(id):
    """Loads user from the databse given the ID

    This is a helper function to `flask-login` that helps in loading a user
    from the database given the ID. Needed because `flask-login` knows nothing
about databses.
    """
    return User.query.get(int(id))

class Post(db.Model):
    """Represents a Blog post created by User of blog app"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.String(140))

    # datetime.utcnow is passed without '()' because the function itself
    # is passed and not the result of calling it
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        """Internal representation of objects of this class"""

        return f'[Post] (title={self.title} created_by={self.user_id})'