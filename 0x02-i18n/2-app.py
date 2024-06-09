#!/usr/bin/env python3
""" Create a / route """
from flask import Flask, render_template, request
from flask_babel import Babel


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
    ''' change language '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """ create the / route """
    return render_template('2-index.html')


if __name__ == '__main__':
    """ run app """
    app.run()
