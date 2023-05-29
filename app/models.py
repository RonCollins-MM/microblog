#!/usr/bin/env python3

"""Contains model classes for the blog app"""

from app import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


class User(db.Model):
    """Represents users of the blog app"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        """Internal representation of objects of this class"""

        return f'[User] (username={self.username} email={self.email})'

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