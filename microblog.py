#!/usr/bin/env python3

"""Main module"""

from app import app, db
from app.models import User, Post

# Decorator ensures that this function is invoked whenever `flask shell`
# is typed in a terminal session
@app.shell_context_processor
def create_shell_context():
    """Creates a context for flask shell session.

    Imports the database instance as well as all the models needed.
    This ensures that the developer has everything setup to begin testing out
    the models in the shell session created.
    """

    context = {
        'db': db,
        'User': User,
        'Post': Post,
    }

    return context