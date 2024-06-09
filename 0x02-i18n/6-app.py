#!/usr/bin/env python3
""" Create a single / route """
from flask import Flask, render_template, request, g
from flask_babel import Babel


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
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
