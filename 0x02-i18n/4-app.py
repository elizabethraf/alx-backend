#!/usr/bin/env python3
"""Display Force locale with URL parameter"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Display Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def helloWorld() -> str:
    """Display Hello world"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """Dispaly local selector"""
    if 'locale' in request.args and request.args
    ['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])
