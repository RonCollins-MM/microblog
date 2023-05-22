#!/usr/bin/env python3

"""Flask app initialisation"""

from flask import Flask

app = Flask(__name__)

from app import routes