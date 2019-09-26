from flask import Flask
from App.models import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://ccq:123@127.0.0.1:3306/day03flask'
    #第一次出现错误：SQLALCHEMY_TRACK_MODIFICATIONS ,那么配置，使其关闭
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app=app)
    return app