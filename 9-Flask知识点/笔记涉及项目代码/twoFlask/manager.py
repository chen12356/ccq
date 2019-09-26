from flask import Flask
from flask_script import Manager
app = Flask(__name__)

#利用命令行参数启动，需要runserver(开发者服务器) -p 端口号 -h 地址 -r 自动重启
manager = Manager(app=app)
@app.route('/') #安某路线分发
def hello():
   return '左边画条龙'

# app.run()
manager.run()