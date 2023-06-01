#!/usr/bin/env python3

"""Defines app routes"""

from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
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
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    """View function for user login

    Authenticated users are redirected to Home page, otherwise login page is
    rendered for user to login.
    """

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('user_login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def user_logout():
    """Logs out user from session"""
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    """Register user to the mircoblog app"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please login to proceed')
        return redirect(url_for('user_login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/users/<username>')
@login_required
def user(username):
    """Load user from database and display in a userprofile html page"""

    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test Post #1'},
        {'author': user, 'body': 'Test Post #2'}
    ]

    return render_template('user.html', user=user, posts=posts)