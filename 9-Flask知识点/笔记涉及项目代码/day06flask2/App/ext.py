from flask_cache import Cache
from flask_migrate import Migrate
from flask_session import Session

from App.models import db

# flask-cache 配置,选择缓存的位置为redis数据库
cache = Cache(config={'CACHE_TYPE': 'redis'})
#注意：如果报错ModuleNotFoundError: No module named 'flask.ext'
#需要修改底层代码，flask.ext.cache 改成flask_cache


def init_app(app):

    #flask_session
    app.config['SECRET_KEY'] = '110'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_KEY_PREFIX'] = 'day06flask'
    Session(app=app)

    #sqlalchemy 模型
    db.init_app(app=app)

    #falsk_migrate  模型迁移
    migrate = Migrate()  #创建模型迁移对象
    migrate.init_app(app=app,db=db) #模型迁移肯定需要模型的

    #初始化cache
    cache.init_app(app=app)




