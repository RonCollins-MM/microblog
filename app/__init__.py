#!/usr/bin/env python3

"""Flask app initialisation"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__) # This helps flask locate resources
app.config.from_object(Config) # Points Flask to the class with config settings
db = SQLAlchemy(app) # Instance of database - represents databse
migrate = Migrate(app, db) # database migration engine
login = LoginManager(app) # login manager instance
login.login_view = 'user_login' # Must tell flask-login which endpoint is being
                                # used for login before using the `@login_required` decorator

# This is done to prevent circular imports
from app import routes, models