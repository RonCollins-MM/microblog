#!/usr/bin/env python3

"""Defines app routes"""

from app import app

@app.route('/')
@app.route('/index')
def index():
    """Handler for home page"""
    return 'Hello World !'