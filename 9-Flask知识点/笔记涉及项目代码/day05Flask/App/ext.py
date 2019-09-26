from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_session import Session

from App.models import db


def init_app(app):

    #flask_session
    app.config['SECRET_KEY'] = '110'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_KEY_PREFIX'] = 'day05flask'
    Session(app=app)

    #sqlalchemy 模型
    db.init_app(app=app)

    #falsk_migrate  模型迁移
    migrate = Migrate()  #创建模型迁移对象
    migrate.init_app(app=app,db=db) #模型迁移肯定需要模型的

    #flask-debugtoolbar
    # app.debug = True
    # debugtoolbar = DebugToolbarExtension()
    # debugtoolbar.init_app(app=app)





