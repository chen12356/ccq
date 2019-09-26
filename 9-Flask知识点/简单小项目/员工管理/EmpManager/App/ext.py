from flask_bootstrap import Bootstrap
from flask_cache import Cache
from flask_migrate import Migrate
from flask_session import Session

from App.models import db

cache = Cache(config={'CACHE_TYPE':'redis'})
def init_ext(app):
    # session
    app.config['SECRET_KEY']='119'
    app.config['SESSION_TYPE']='redis'
    app.config['SESSION_KEY_PREFIX']='python1905'
    Session(app=app)

    # sqlalchemy
    db.init_app(app=app)

    # migrate
    migrate = Migrate()
    migrate.init_app(app=app,db=db)

    # flask-bootstrap
    Bootstrap(app=app)


    # flask-debugtoolbar
    # app.debug = True
    # debugtoolbar = DebugToolbarExtension()
    # debugtoolbar.init_app(app=app)


    # flask-cache
    # 如果cache在方法内 那么导包是不可以的  需要将这个遍历防到方法外
    # cache = Cache(config={'CACHE_TYPE':'redis'})
    # 如果报错 ImportError: No module named 'flask.ext'
    # 解决方法：（1）打开site-packages
    #          (2) flask-cache下的jinja2ext.py
    #          (3) 修改from flask.ext.cache import make_template_fragment_key为
    #      from flask_cache import make_template_fragment_key
    cache.init_app(app=app)