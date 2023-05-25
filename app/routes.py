#!/usr/bin/env python3

"""Defines app routes"""

from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    """View function for user login

    Renders the user login form
    """

    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Attempted login for {form.username.data} [remember_me:{form.remember_me.data}]')
        print(f'Attempted login.\n[Username={form.username.data} '\
              f'Password={form.password.data} Remember_me={form.remember_me.data}]')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)