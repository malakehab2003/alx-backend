#!/usr/bin/env python3
""" Create a single / route """
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz import exceptions


class Config:
    """ Configuration for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """ determine the best language """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    user = g.get('user')
    if user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']

    header = request.headers.get('locale')
    if header and header in app.config['LANGUAGES']:
        return header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ determine the best time zone """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except exceptions.UnknownTimeZoneError:
            pass

    user = g.get('user')
    if user:
        timezone = user.get('timezone')
        if timezone:
            try:
                pytz.timezone(timezone)
                return timezone
            except exceptions.UnknownTimeZoneError:
                pass
    header_time = request.headers.get('timezone')
    if header_time:
        try:
            pytz.timezone(header_time)
            return header_time
        except exceptions.UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """ get the logged in user """
    user = request.args.get('login_as')
    if user and int(user) in users.keys():
        return users[int(user)]
    return None


@app.before_request
def before_request():
    """ before request """
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index():
    """ create the / route """
    timezone = get_timezone()
    return render_template('7-index.html', timezone=timezone)


if __name__ == '__main__':
    app.run()
