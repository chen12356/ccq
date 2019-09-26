from flask import Flask
app = Flask(__name__)

@app.route('/') #安某路线分发
def hello():
   return '左边画条龙'

app.run()
