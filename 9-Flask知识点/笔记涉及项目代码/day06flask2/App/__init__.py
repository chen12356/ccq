from flask import Flask

from App import settings
from App.ext import init_app
import os

#处理template与static问题，原先是在App文件下，现在迁移到项目目录下
templates = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'templates')
static = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'static')


def create_app(env_name):
    app = Flask(__name__,template_folder=templates,static_folder=static)
    app.config.from_object(settings.ENV_NAME.get(env_name))

    init_app(app)
    return app
