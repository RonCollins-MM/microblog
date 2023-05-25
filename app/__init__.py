#!/usr/bin/env python3

"""Flask app initialisation"""

from flask import Flask
from config import Config

app = Flask(__name__) # This helps flask locate resources
app.config.from_object(Config) # Points Flask to the class with config settings

from app import routes # This is done to prevent circular imports