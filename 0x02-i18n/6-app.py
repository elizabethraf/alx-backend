#!/usr/bin/env python3
"""display Use user locale"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Display Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """Display user"""
    g.user = get_user(request.args.get("login_as"))


@babel.localeselector
def get_locale():
    """Display local host"""
    if 'locale' in request.args and request.args
    ['locale'] in app.config['LANGUAGES']:
        return request.args['locale']

    if hasattr(g, 'user') and g.user.locale in app.config['LANGUAGES']:
        return g.user.locale

    locale = request.headers.get('Accept-Language')
    if locale:
        return locale

    return app.config['BABEL_DEFAULT_LOCALE']
