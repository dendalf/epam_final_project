""" Views index file for library_app """
# pylint: disable=invalid-name, cyclic-import
from datetime import datetime

from flask import render_template

from library_app import app, logger


@app.route('/')
def index():
    """ Home page """
    logger.log('Home page was requested')
    return render_template('index.html', title='Home page', content='Welcome to Library!')