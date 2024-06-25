#!/usr/bin/env python3
"""Basic Flask app that implements i18n and internationalization"""

from flask import Flask, render_template, request
from flask_babel import Babel, get_locale, get_timezone

app = Flask(__name__)


class Config:
    """Config class for your application, it deals with babel mostly"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)



def get_locale():
    """Get locale for your application"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])
babel.init_app(app, locale_selector=get_locale)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Home page for your application"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
