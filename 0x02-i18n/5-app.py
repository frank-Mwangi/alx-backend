#!/usr/bin/env python3
""""Basic Babel setup"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    requested_locale = request.args.get('locale')
    if requested_locale:
        return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def home():
    """The homepage"""
    return render_template("5-index.html")


@app.before_request
def before_request():
    """set user"""
    g.user = get_user()


def get_user():
    """Validate user function"""
    key = request.args.get('login_as')
    return users[int(key)] if key and int(key) in users.keys() else None


if __name__ == "__main__":
    app.run()
