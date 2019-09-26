from flask import Flask

from App import settings
from App.ext import init_app


def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(settings.ENV_NAME.get(env_name))

    init_app(app)
    return app
