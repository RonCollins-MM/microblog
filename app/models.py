#!/usr/bin/env python3

"""Contains model classes for the blog app"""

from app import db

class User(db.Model):
    """Represents users of the blog app"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        """Internal representation of objects of this class"""

        return f'[User] (username={self.username} email={self.email})'