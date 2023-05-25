#!/usr/bin/env python3

"""Contains all the configuration settings for this flask app"""

import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Configuration for the microblog app"""

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-hard-to-guess-string'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(base_dir, 'app.db')

    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
