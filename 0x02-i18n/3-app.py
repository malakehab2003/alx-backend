#!/usr/bin/env python3
""" Create a single / route """
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """ Configuration for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)


@babel.localeselector
def get_locale():
    """ determine the best language """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """ create the / route """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
