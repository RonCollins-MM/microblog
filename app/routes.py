#!/usr/bin/env python3

"""Defines app routes"""

from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    """Handler for home page"""
    user = {'username': 'Roncollins'}
    posts = [
        {
            'author': {'username': 'muelsy'},
            'body': 'To be or not to be ....'
        },
        {
            'author': {'username': 'Dr. Suess'},
            'body': 'The cat sat on the mat'
        }
    ]
    return render_template('index.html', user=user, title='Home', posts=posts)