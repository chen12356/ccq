from flask import Blueprint, request, current_app, render_template

from App.ext import cache

blue = Blueprint('blue',__name__)

@blue.route('/index/')
def index():
    return 'xxxx'

#=========================
#cache 的使用
#第一种
@blue.route('/helloCache/')
#使用cache装饰器缓存，参数timeout是第一次之后每次请求生效的时长。单位s
@cache.cached(timeout=10)
def helloCache():
    print('会等10s ? ')
    return '2003年第一场雪'
#第二种
@blue.route('/testCache/')
def testCache():
    value = cache.get('ip')  #先查找是不是在cache缓存中
    if value:
        return '你又来了--%s'%value
    ip = request.remote_addr  #获取请求的ip
    cache.set('ip',ip)  #set方法存放到cache中，前者设置值的键，后者值
    return '欢迎光临……'

#===================================
# 钩子
# aop 面向切面编程，减少代码冗余、解耦合
#例子：假设，在视图中对数据库进行操作，是不是都要链接数据，增删改查，那么
#使用钩子，单独把链接数据库提出来，在请求发生之前，先帮你执行咯 (也可以封装，不理想)
@blue.before_request
def beroreRequest():
    print('我在你们发生请求之前已经帮你们链接好数据库了^^')
#在下面发生请求之前，上面已经执行了，解耦合
@blue.route('/add/')
def add():
    return 'add'
@blue.route('/delete/')
def delete():
    return '删除'
@blue.route('/update/')
def update():
    return '更新'
@blue.route('/find/')
def find():
    return '查询'

#====================================
# 四大内置对象
#request
#session
#上面两者前几天介绍了，下面来介绍下面两种
#config ==> 两种用法，在模板中(如testConfig.html)与在Python中
#g  ==> A视图函数获取B视图函数的值，前提B视图函数先执行，才可执行A，否则报错

#config ==> Python使用
@blue.route('/pyConfig/')
def pyConfig():
    for c in  current_app.config:
        print(c)
    return 'python 中的config对象的值'
#页面中config
@blue.route('/testConfig/')
def testConfig():
    return render_template('testConfig.html')

#使用g
@blue.route('/g/')
def g():
    g.ip = request.remote_addr
    return 'g'
@blue.route('/testG/')
def tsetG():
    print(g.ip)  #获取另一个视图函数的ip值，需要使用g，前提另一个有g.ip值
    return 'testG'

#=========================================
# templates 和 static的路径问题
#把模板和静态资源文件夹放到项目的目录下，因为一个项目不止1个App，这样可以让多个App继承模板
@blue.route('/path/')
def path():
    return render_template('path.html')