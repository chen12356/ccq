from flask import Flask

from App import settings
from App.ext import init_app


#处理template与static问题，原先是在App文件下，现在迁移到项目目录下
from App.urls import init_urls

def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(settings.ENV_NAME.get(env_name))

    init_urls(app)
    init_app(app)
    return app
