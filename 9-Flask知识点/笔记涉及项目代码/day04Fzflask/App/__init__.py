from flask import Flask

from App import setting
from App.ext import init_ext


def create_app(env_name):
    app = Flask(__name__)

    app.config.from_object(setting.ENV_NAME.get(env_name))

    init_ext(app)
    return app