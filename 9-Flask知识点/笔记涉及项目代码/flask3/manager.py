from flask_script import Manager
from App import create_app
from App.views import blue

app = create_app()

#注册蓝图,参数的值blue是由views.py 中导入的,
app.register_blueprint(blueprint=blue)

#将app交给Manager
manager = Manager(app=app)

if __name__=="__main__":
    manager.run()
