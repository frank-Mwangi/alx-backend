#!/usr/bin/env python3
""""Basic Babel setup"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """The configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel.init_app(app)


@babel.localeselector
def get_locale():
    """Set language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home():
    """The homepage"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
