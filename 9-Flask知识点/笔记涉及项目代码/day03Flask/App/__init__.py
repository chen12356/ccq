from flask import Flask
from flask_session import Session


def create_app():
    app = Flask(__name__)
    #配置secret_key ==> flask把session的key存储在客户端cookie中，通过这个
    #key可以从flask的内存中获取。出于安全考虑使用secret_key进行加密处理，先设置其值
    app.config['SECRET_KEY'] = '110'

    app.config['SESSION_TYPE'] = 'redis' #保存到了redis中

    app.config['SESSION_KEY_PREFIX'] = 'flask_day03' #保存在redis的对象名
    Session(app=app)
    return app