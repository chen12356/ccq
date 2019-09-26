from flask import Blueprint, render_template

#需要注意的是，蓝图的导入从flask模块导入的，并不是flask-blueprint中导入的


#创建Blueprint对象，注意在views.py中创建的对象，因为在需要解决路由问题
blue = Blueprint('blue',__name__)

#@app.route('/test/')  ==>这是路径问题，利用蓝图来解决
@blue.route('/test/')   #此时就不是用@app.route来设置路由的
def test():
    return 'hello'

@blue.route('/testreturn/')  #返回html页面
def testreturn():
    return render_template('testreturn.html')