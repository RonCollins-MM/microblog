#!/usr/bin/env python3

"""Contains all the configuration settings for this flask app"""

import os

class Config(object):
    """Configuration for the microblog app"""

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-hard-to-guess-string'
