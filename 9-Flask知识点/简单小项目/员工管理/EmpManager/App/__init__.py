from flask import Flask

from App import settings
from App.ext import init_ext

import os


def create_app(envname):
    app = Flask(__name__)

    app.config.from_object(settings.ENV_NAME.get(envname))

    init_ext(app)

    return app