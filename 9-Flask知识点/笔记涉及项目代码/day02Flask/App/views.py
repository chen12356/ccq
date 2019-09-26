import uuid

from flask import Blueprint, render_template, redirect, url_for, request, session

blue = Blueprint('blue',__name__)


#设置路由参数--默认字符串
@blue.route('/test1/<id>/')
def test1(id):
    print(id)
    return 'tianqizhenghao'
#path ==> 会把/当作字符处理，但是string ==>会把/ 当作结束标志
@blue.route('/test2/<path:name>/')
def test2(name):
    print(name)
    return 'test2'
#int、float、与上面两种用法是一样的。int是整型、float浮点型

#uuid ==> 需要先生成 uuid,
@blue.route('/testuuid/')
def testuuid():
    uid = uuid.uuid4()
    print(uid)  #如459e790c-b9b9-4431-99b0-4be1eb006721
    return 'xx'
#访问：127.0.0.1:5000/test3/459e790c-b9b9-4431-99b0-4be1eb006721
@blue.route('/test3/<uuid:uid>/')
def test3(uid):
    print(uid)
    print(type(uid)) # <class 'uuid.UUID'> uuid类型，也是一种格式
    return 'xxxxx'
#any ==> any(a,b):p ==>指的是参数的值a或者b，也就是你访问的时候可以使用参数a、b或c
@blue.route('/test4/<any(a,b,c):p>/')
def test4(p):
    print(p)
    print(type(p))  # ==> str
    return 'any(a,b,c):p'
#==============================================

#反向解析: url_for(‘蓝图名字.方法名’) ==>得到该方法的请求资源路径
@blue.route("/test5/")
def test5():
    p = url_for("blue.test4",p='a')  #该方法有参数，那么在这里第二个参数，就是该方法的变量参数
    s = url_for('blue.tologsession')  #该方法没有参数
    print(p)  # /test4/a/  ==>拼接了参数
    print(s)  # /tologsession/
    return  p
#===============================================

#请求request  ==>11种
'''写法：request.方法 ==> request.method
method ==> 获取请求方式 /http(可以前后分离)
base_url  ==> 得到资源路径 (不显示参数) (注意：该参数不是指路由参数)
hosr_url ==> 只得到主机的路径(不包括资源路径)
url     ==> 得到完整的 url 路径
remote_addr  ==> 得到访问主机地址(用于反爬)
files   ==> 上传文件(比如一些头像等)
headers ==> 返回请求头
path  ==> 请求资源路径  (比如：不登录，不能进入购物车，这是购物车就需要判断了)
cookies   ==>获取请求的cookie

两种比较重要的：
args  ==> 获取get请求的值(一个大列表，列表元素是元组-->(key，value))
	#https://127.0.0.1:5000/testRequest/?name=zs&age=18&age=19
	print(request.agrs)  ==> 得到是个列表，列表元素是元组-->(key，value)
#如何获取name的值
	name = request.args.get('name')   ==> zs
	age = request.args.get('age')   ==> 18 ,遇到第一个就返回了。不会返回19
#如果向获得18、19呢 ==> 利用getlist
	age_list = request.args.getlist('age')  
	
form  ==> 获取post请求的值，post基于form表单来发送的(在表单中需要规定method)
    #post 请求  --> form  ==> post 都是通过表单来发的。
	name2 = request.form.get('name')
	age2 = request.from.getlist('age')
'''
@blue.route('/test6/',methods=['get','post'])
def test6():
    #比如访问：http://127.0.0.1:5000/test6/?name=zs&age=19&age=22
    s1 = request.method
    s2 = request.base_url
    s3 = request.host_url
    s4 = request.url
    print(s1)  # GET
    print(s2)  # http://127.0.0.1:5000/test6/
    print(s3)  #http://127.0.0.1:5000
    print(s4)  #http://127.0.0.1:5000/test6/?name=zs&age=19&age=22

    #利用 args 来处理get
    name = request.args.get('name')
    print(name)
    age_list = request.args.getlist('age')  #getlist 得到同名参数的所有值,列表的形式
    print(age_list)

    #同样处理post，注意post参数不再url地址上传递，需要利用表单,在这我们利用postman工具来实现post
    name2 = request.form.get('name')   #下面的例子存在 form 使用
    age_list2 = request.form.getlist('age')
    print(name2)  #有表单才有值
    print(age_list2)
    return s1
#================================================


#========================================
# 使用cooike
# @blue.route('/tologincookie/')
# def tologincookie():
#     return render_template('logincookie.html')
#
#
# @blue.route('/logincookie/',methods=['post'])
# def logincookie():
#     name = request.form.get('name')
#     print(name)
#     response = redirect(url_for('blue.welcomecookie'))
#     #设置cookie
#     response.set_cookie('name',name)
#     return response
#
# @blue.route('/welcomecookie/')
# def welcomecookie():
#     #获取cookies中的值
#     name = request.cookies.get('name','游客')
#     print(name)
#     return render_template('welcomecookie.html',name=name)
#
# #点击退出,其路由找到这，执行下面的视图函数
# @blue.route('/logoutcookie/')
# def logoutcookie():
#     #由于需要删除cookie对象，我们需要response对象
#     response = redirect(url_for('blue.welcomecookie'))
#     #删除cookie
#     response.delete_cookie('name')
#     return response
# =========================================

#使用session
@blue.route('/tologsession/')
def tologsession():
    return render_template('logincookie.html')

@blue.route('/logincookie/',methods=['post'])
def logincookie():
    name = request.form.get('name')
    session['name'] = name
    return redirect(url_for('blue.welcomesession'))

@blue.route('/welcomecookle/')
def welcomesession():
    name = session.get('name','MM')
    print(name)
    return render_template('welcomecookie.html',name=name)

@blue.route('/logoutcookie/')
def logoutsession():
    response = redirect(url_for('blue.welcomesession'))
    #session.pop('name') #弹出name,直到获取的值弹完，报错
    response.delete_cookie('session') #删除原先name,会一直是默认的值
    return response