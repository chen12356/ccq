from flask_migrate import Migrate
from flask_session import Session

from App.models import db


def init_ext(app):
    # flask-session
    app.config['SESSION_KEY'] = '110'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_KEY_PREFIX'] = 'python1905'
    Session(app=app)

    # flask-sqlalchemy
    # app.config['SQLALCHEMY_TRACK_MODIFICAITIONS'] = False
    # app.comfig['SQLACHEMY_DATABASE_URI'] = 'mysql+pymysql://ccq:123@localhost:3306/day04flask'

    db.init_app(app=app)

    #flask-migrate，先创建对象，然后初始化，参数app与db，讲app与模型传给migrate
    migrate = Migrate()
    migrate.init_app(app=app,db=db)