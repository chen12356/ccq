### 一、请求request

+ request --- 一个内置对象（不需要创建就可以直接使用的对象，直接导入，还有session）

+ ```
  @blue.route('/testRequest/',methods=['get','post'])
  def request():
  	pritn(request)  ==>得到是个对象。导入：from flask.globals import request 
  	
  	#获取的请求方式 /http  方法   ==>前后端分离
  	print(request.method)
  	
  	#去掉参数的请求资源路径(也就是传的参数不显示)
  	print(request.base_url)
  	
  	#主机的路径，不带请求资源路径
  	print(request.host_url)
  	
  	#完整的url路径,(请求资源路径和请求参数)
  	print(request.url)
  	
  	#返回主机地址(可以应用于反爬虫) 
  	print(request.remote_addr)
  	
  	#文件上传(比如注册的需要上传头像等，就是用这个)
  	print(request.files)
  	
  	#返回请求头(访问服务器需要携带一些参数)
  	print(request.headers)
  	
  	#请求资源路径  (比如：不登录，不能进入购物车，这是购物车就需要判断了)
  	print(request.path)
  	
  	#获取请求的cookie
  	print(request.cookies)     ==>得到字典
  	
  	
  	#get 请求   --> args
  	#https://127.0.0.1:5000/testRequest/?name=zs&age=18&age=19
  	print(request.agrs)  ==> 得到是个列表，列表元素是元组-->(key，value)
  	#如何获取name的值，
  	name = request.args.get('name')   ==> 该'name'是标签的属性值。zs
  	age = request.args.get('age')   ==> 18 ,遇到第一个就返回了。不会返回19
  	#如果向获得18、19呢 ==> 利用getlist
  	age_list = request.args.getlist('age')  
  	
  	
  	#post 请求  --> form  ==> post 都是通过表单来发的。可以使用postman工具中实现表单的操作，用于练习。
  	name2 =. request.form.get('name')
  	age2 = request.from.getlist('age')
  	
  	print(session)  ==> 不属于 request的，直接从flask.globals导入
  	
  	
  	return 'request'
  ```

+ 端口号

  ```
  数据库默认端口号： mysql 3306
  				mongodb  27017
  				Oracle   1521
  				redis    6379
  协议默认端口号：   http  80   
              	https  443
              	ftp  21
             		ssh  22
  ```

### 二、响应 response

+ 视图函数的返回值 5 种

```
1.字符串
2.render_template
3.make_response()
4.redirect
5.Response
```

+ 返回字符串

  + ````
    @blue.route('/testResponse/')
    def response():
    	return '床前明月光'
    ````

+ 返回一个模版html

  + ```
    @blue.route('/testResponse1/')
    def response1():
    	r = render_template('response.html')  ==> 在template文件夹下的
    	return  r  ==> 也是字符类型
    ```

+ 返回一个 **make_response()**

  + 需要在 flask中导入 make_response

  + ```
    @blue.route('/testResponse2/')
    def response2():
    	r = make_response('<h1>家有儿女</h1>')
    	print(type(r))  ==> 返回的是 response对象
    	return r
    ```

+ 返回一个 **redirect**   重定向

  + 需要从flask导入 redirect 

  + ```
    @blue.route('/index/')
    def index():
    	return 'hello word'
    @blue.route('/testResponse3/')
    def response3():
    	#硬编码的形式
    	# r = redirect('/index/')  ==> 此时定向到 index
    	#利用反向解析
    	r = redirect(url_for('blue.index'))  ==> 同样也是response对象
    	return r
    ```

+ 返回一个**Response **  和make_response差不多一样的，只是Response是个类，继承一个类，方法属性比较多。

  + ```
    @blue.route('/testResponse4/')
    def response4():
    	r = Response('低头思故乡')  ==> 也是response对象
    	return r
    ```

+ 总结

```
视图函数的返回值有2大类:
1.字符串 对象  ==> string、render_template  ==> 页面也是字符串

2.response 对象  ==> make_response、redirect、Response 
```

### 三、异常

+ 虽然代码简单，实则不知道用在哪,

需要在 flask 导入 **abort**

```
@blue.route('/testAbort/')
def abort():
	#抛出异常(状态码)
	abort(404)
	
	return "hello abort" 

//如何处理异常呢？
@blue.errorhandler(404)   ==>对应抛出异常的状态码
def testAbort(Exception):  ==> 处理异常的函数，需要参数:Exception
	return '系统正在升级，请稍后再试...'
```

+ 流程：  利用abort 抛出异常状态码 ==>利用errorhandler(状态码)，捕捉异常状态码 ==>执行对应的处理函数(参数：Exception)

### 四、会话

+ 第一次请求：

  当浏览器访问服务器==>服务器会 先创建 session 对象 ，该对象有一个属性叫做 session_key 其值是唯一的 ===> 服务器会返回：set_cookie消息头(就是session_key)  ===> 此时浏览器会得到session_id （和服务器的叫法不一样，一样的东西）。

+ 第二次请求：

  在浏览器第二次请求时，会携带者session_id 取服务器 寻找 。如果找到，说明已经登录过的，如果没有找到，那么需要重新登录该服务器。

短连接 ==> 一次请求，一次响应

利用会话技术，延长交互的生命周期，实现多个请求，多次响应。记录关键的数据记录(比如登录信息)  ==> 但是这些记录都是保存在 浏览器/客户端(cookie)  ==> session 是服务器 的状态管理技术(cookie是客户端的状态管理技术)

#### 1、cookie

+ 客户的会话技术，所有的数据都保存在客户端中，服务器不做任何存储

+ 特点

  + 支持过期时间
    + max_age  毫秒
    + expries     具体日期
  + 更加域名进行cookie存储  (比如淘宝值保存淘宝，更加域名)
  + 不能跨网站 （各网站保存各网站的记录）
  + 不能跨浏览器
  + 自动携带 本网站的所有cookie

+ cookie的创建  ==> (服务器创建)  服务器操作客户的数据 （因为session对象是在服务器创建的）

+ cookie使用

  + ```
    设置cookie  response.set_cookie('username',username)
    
    获取cookie   username = request.cookies.get('username','游客')
    
    删除cookie   response.delete_cookie('username')
    ```

  + 案例：执行一 个视图函数，跳转到一个页面logincookie.html，然后输入一个用户名字xxx，点击提交，然后跳转到 welcomecookie.html ,  该页面的内容：欢迎xxx 。

    如果没有经过登录， 直接跳转到welcomecookie.html ,显示 欢迎游客

    如果已经登录过，跳转到welcomecookie.html页面，那么在欢迎xxx的下面还有一个退出，点击退出， 跳转到welcomecookie.html页面，显示欢迎

  ```
  @blue.route('/toLogincookie/')
  def tologincookie():
  	return render_template('logincookie.html')
  	
  @blue.route('/logincookie/',methods=['post'])
  def logincookie():
  	name = request.form.get('name')  ==> 获取post请求，得到表单中name属性对应的值
  	response = redirect(url_for('blue.welcomecookie'))  ==>设置cookie是需要有一个response对象，利用redirect方法(重定向,重新执行一个请求来渲染页面)
  	response.set_cookie('name',name)  ==> 设置cookie对象，前提需要有response对象
  	return response   ==> 返回该对象
  	
  @blue.route('/welcomecookie/')
  def welcomecookie():
  	name = request.cookies.get('name','游客')  ==>获取cookie对象的值
  	
  	return render_template('welcomecookie.html',name=name) ==>在render_template方法中，有个默认参数context==>上下文,让模版和视图函数建立关联。（前者是模版的{{ name }} , 后者是 视图函数中的name 值，把这传给了模版）
  ```


#### 2、session

服务器端的会话技术 ----->session存储在服务器中。

所有数据存储在服务器中、默认存在服务器的内存中(关机就没了指的就是内存)、存储结构也是key-value形式，键值对。

​		Django对session做了持久化，把数据写到了数据库里面。

注意：在flask中单纯使用session会报错的。需要使用在`__init__`方法中配置：

​			`app.config['SECRET_KEY']='110'`

​	为啥：因为flask把session的key存储在客户端的cookie中，

+ session的使用 

  + ```
    //前两者用作登录
    设置：session['username'] = username
获取：session.get('username')
    
    //删除用作与退出
    删除：session.pop('username')  ==> 弹出session中，空了就报错(可以设置条件判断)
    	 response.dalete_cookie('session')  ==> 利用cookie来删除(不会报错)
    ```
    
  + 同上的案例：
  ```
  #使用session   在views.py中
  //实现登录
  @blue.route('/tologsession/')
  def tologsession():
      return render_template('logincookie.html')
  
  //设置post请求，获取表单的值，设置session对象
  @blue.route('/logincookie/',methods=['post'])
  def logincookie():
      name = request.form.get('name')
      session['name'] = name  ==>设置session对象
      return redirect(url_for('blue.welcomesession'))
  
  //将得到的session对象的值取出来，传递给指定的html，
  @blue.route('/welcomecookle/')
  def welcomesession():
      name = session.get('name','MM')  ==>获取session的值，后面设置的是默认值
      print(name)
      return render_template('welcomecookie.html',name=name) ==>将name传给页面
  
  //退出页面的，也就是删除session对象的例子
  @blue.route('/logoutcookie/')
  def logoutsession():
      response = redirect(url_for('blue.welcomesession'))
    #下面是两种删除session的方法。
      #session.pop('name') #弹出name,直到获取的值弹完，报错
      response.delete_cookie('session') #删除原先name,会一直是默认的值(不报错)
      return response
  ```
  

#### 3、cookie和session总结

+ cookie:客户端浏览器的缓存；session： 服务端服务器的缓存
+ cookie 不是很安全，别人可以分析存放在本地的cookie并进行 cookie 欺骗，考虑到安全的应当使用session.
+ session会在一定时间内保存在服务器上。当访问增多的，会比较占用服务器的内存，影响性能，所以，可以把重要信息放在session里面，其他信息可以放在cookie中。

#### 4、session持久化问题

+ 在Django中，对session做了持久化，存储在数据中

+ 在 flask中 没有对session进行任何处理

  + 需要模块：flask-session 可以实现session的数据持久化
  + 其位置实任意的，但是更推荐使用 redis
  + 缓存在磁盘中，管理磁盘使用的是：**lru**(**最近最少使用原则**)，
    + 假如一个磁盘中，有多个分片，当又来一个，磁盘放不下了，会把最少了去掉，没有最少就把最近的删掉

+ 步骤

  + 安装：`pip install flask-session`

    + `pip install redis `  ==> 在虚拟环境导入 redis

  + 代码及步骤：
  
    + 初识化----创建 session对象
    + 配置-- app.config['SECRET_KEY'] = '110'
    + 持久化位置 -- [ SESSION_TYPE] = 'redis'
    + 其他配置，如存入redis中的名 --['SESSION-KEY_PREFIX']  = '别名'
    
    ```
    //完整一个过程：
    
    def create_app():
    	app = Flask(__name__)
    	app.config['SECRET_KEY']= '110'
    	#如果报错No module named 'redis' 那么证明虚拟环境没有redis模块
    	#需要手动安装 pip install redis
    	#session生命周期31天，Django是14天
    	
    	app.config["SESSION_TYPE"] = 'redis'  ==>持久化位置(session放在哪)
    	
    	#session加前缀,可以在redis中通过 ：key *  查看redis中session对象
    	app.config['SESSION_KEY_PREFIX'] = 'python1995'
    	
    	#初始化，创建session对象，有两种
    	Session(app=app)  ==> 第一种
    	
    	#se = Session()  ==> 第二种
    	#se.init_app(app=app)
    	
    	return app
    ```
    
  + 查看redis中的内容
  
    + ```
      运行redis，并给定一个配置文件(redis.conf先从包里复制到下面的路径里)
      sudo redis-server /usr/local/etc/redis.conf  ==>启动redis服务器
      redis-cli  ===> 进去redis
      keys *    ===>查看redis的所有key
      get key       		 	
      ttl session   -->31天
         flask的session的生存时间是31天，django的session生存时间是15天
      ```

### 五、模版 template

13年，h5出来，兼容性很强，可以供多个平台适应，比如一个前端，多个后端，那么前端和后端通过json进行对接。（**json**：是一个轻量级(比xml解析速度快，体积小)的数据交换标准（相当于媒介））

所以：在static中 不能写一些后端的内容，比如{{}}  {% %} ，等，前端不认识，只能写在template。

前后端分离项目 == > js

全栈  ==> template

+ 简介

  ```
  1、MVC中的view，MTV中的Template
  2、主要用来做数据展示的
  3、过程分为2个阶段
  	加载
  	渲染
  4、jinja2模版引擎 （完全抄袭Django的语法，多个一个宏定义）
  	本质上是html
  	支持特定的模版语法
  	flask 作者开发的 
  	jinja2的优点
  		速度快、html与后端python的分离、减少Python的复杂度、灵活、提供了控制，继承等功能。
  
  ```

+ 语法使用

  ```
  //
  @blue.route('/index/')
  def index():
  	#优化问题：页面接收   视图函数没有传递
  			 视图函数传递， 页面没接收
  	return render_template('index.html',age=18,sex='n')
  ```
  
+ template中的文件 index.html
  
  ```
    //模版文件 如：省略……
    <body>
        {{ name}}
    </body>
  ```
  
  + 基模版  base.html

    ````
  …………
    <head>
    	<meta char……>
    	<title ……>   
    	{% block ext_css %}
    	
    	{% endblock %}
    
    </head>
    
    <body>
    	{% block header %}
    	{% endblock %}
    	
    	{% block content %}
    	{% endblock %}
    	
    	{% block footer %}
    	{% endblock %}
    	
    	{% block ext_js %}   ==> 放入到body的最下面，在加个cdn，让js加载更快
    	{% endblock %}
    </body>
    
    ````
    
    78-85kb之间，
  + 继承基模版    
  
    如base_a.html
  
  ````
    {% extends 'base.html' %}  ==>继承语句
  
    {% block header %}   ==> 填坑
    	排行 
    {% endblock %}
  
    {% block footer %}     ==> 结构 footer 中，include引入 base_x.html 
    	{ include 'base_x.html' }  
    	aiff
    {% endblock %}
  
  ```
  + base_b.html
  
    ```
    {% extends 'base_a.html' %}
  
    {% block header %}
    	{{ super() }}  ==> 当子模版中有和父模版中重名，那么不会覆盖父模版的值,避免覆盖
    	飞龙在天
    {% endblock %}
    
    ```
  + 如：base_x.html 
  
    ```
    {% extends 'base.html' %}
  
    {% block header %}
    	{{ super() }} 
    	aiff
    {% endblock %}
    ```
  
  
    ```
  
    ```
  
+ 宏定义

  + 三种：无参数、有参数、其他页面导入

  ```
  @blue.route('')
  ```

  macro.html

  ```
  其他忽略
  <body>
  	{# 无参数的 宏定义 macro #}  ==> 该注释，源码显示不了
  	{% macro say() %}   ==>定义了say方法，如何调用呢？
  		严惩不贷
  	{% endmacro %}
  
  	{{ say() }}  ==>调用上面定义的函数
  	{{ say() }}
  
  	
  	{% marco getUser(name,age) %}
  		{{ name }} 的年龄 {{ age }}
  	{% endmarco %}
  	{{ getUser('张三','16') }}  ==> 调用时传参数
   
   
   	{# 引用其他文件定义macro #}
      {% from '文件名.html' import 宏方法 %}
      {{ 宏方法() }}  ==> 调用导入进来的方法
      
  <body>
  ```

  如：tomarco.html

  ```
  <body>
  	{% macro getName(name) %}
  	{% endmacro %}
  <body>
  ```

+ 循环控制  for - if语句

  + 同样在view中设置路由 

    ```
    @blue.route('/testFor/')
    def testFor():
    	#比如 有个列表
    	score_list = [53,53,22,233,53]
    	
    	return render_template('testFor.html')
    ```

  如：testFor.html

  ```
  其他忽略
  <body>
  	<ul>
  		{% for score in score_list %}  ==>for循环,将视图函数值传过来
  			<li>{{ score }}</li>
  		{% endfor %}
  	</ul>
  	<hr>
  	
  	for 循环加 if 语句   ==>重要
  	<ul>
  		{% for score in score_list %}
  			{% if loop.first %}  ==> loop.first (第一个值)
  					<li style="color:green">{{ score }}</li>
  				{% eilf loop.last %}
  					<li style="color:red">{{ score }}</li>
  				{% else %}
  					<li style="color:pink">{{ score }}</li>
  			{% endif %}
  		{% endfor %}
  	</ul>
  	<hr>
      {% for score in scores %}
          {# loop.index 返回序号，默认从1开始，如果index0-->从0开始 #}
          {{ loop.index }}
      {% endfor %}
      <hr>
      {% for score in scores %}
          {# loop.index 返回序号，默认从1开始，如果index0-->从0开始 #}
          {{ loop.index0 }}
      {% endfor %}
      <hr>
      {% for score in scores %}
          {# loop.revindex 返回序号（倒序）-->到1结束，如果revindex0-->到0结束 #}
          {{ loop.revindex }}
      {% endfor %}
          <hr>
      {% for score in scores %}
          {# loop.revindex 返回序号（倒序）-->到1结束，如果revindex0-->到0结束 #}
          {{ loop.revindex0 }}
      {% endfor %}
  	
  </body>
  ```

+ 过滤器

  + 先设置视图函数

    ```
    @blue.route('/testFilter/')
    def testFilter():
    	code = 'abcdefg'
    	code1 = 'abcd    '
    	code2 = '<h1>你好</h1>'
    	return render_template('testFilter.html',code=code,code1=code1)
    ```

  如：testFilter.html

  ```
  <body>
  	<hr>
  	{{ code|upper }}
  	<hr>
  	{{ code|upper|lower}}
  	<hr>
  	{{ code1|trim|reverse}}   ==>trim 去除空格，中间空格去除不了，reverse反转
  	
  	<hr>
  	{{ code2}}  ==>原样输出
  	{{ code2|striptags}}  => 去除标签，
  	{{ code2|safe }}  ==> safe 标签生效
  </body>
  ```



### 六、模型 models

+ 简介

```
数据交互方法的封装  -->  与表一一对应
flask中并没有提供任何数据库操作的API(接口)
因此flask有两种方式：
	1、原生SQL缺点：
		1、代码利用率低，条件复杂代码语句过长，有很多相似语句
		2、修改一些sql语句，需要了解业务逻辑，相当麻烦
	2、选择ORM(对象关系映射)  ==> 把对象的操作转为对数据库的操作
	解决：很多语言都对其操作进行封装。
	在flask可以用sqlalchemy，mongoEngine(比较少用的)
	利用sqlalchemy：
		其优点：
            1.易用性、可以有效减少重复的sql语句
            2.性能消耗少
            3.设计灵活、可以轻松实现复杂查询
            4.移植性好
```

+ sqlalchemy

  + sqlalchemy就是用来操作数据库的工具 ---> 其实就是对  **pymysql的再一次封装**
  + 基本配置：

  ```
  1、安装： pip install flask-sqlalchemy
  
  2、创建sqlalchemy对象
  	第一种：db = SQLAlchemy(app=app)
  	第二种：db=SQLALchemy()	-->建议
  比如：
  	写在models.py中
  		from 导入该模块
  		db = SQLAlchemy()
  	
  	在init.py中使用db, 需要从models.py中导入
  		db.init_app(app=app)  -- 初始化
  	
  	
  3、config中配置(在App中__init__中 )
  	#dialect方言,dirver驱动，注意：URI
  	app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123@localhost:3306/数据库名'
  	
  4、创建表，在views.py中，写个视图函数，在views中创建
  如：
  @blue.route('createTable')
  def createTable():
  	db.create_all()  ==> 创建表，方法 create_all
  	return '创建成功'
  ```

  用sqlalchemy创建表  ===> 把模型类变成一张表

  + models.py

  ```
  from flask_sqlalchemy import SQLAlchemy
  db = SQLAlchemy()
  
  //比如一个动物类
  class Animal(db.Model):  ==>需要继承Model
  	#id 是否要写？ -- 必须要写
  	id = db.Column(db.Integer,primary_key=True,auto_increment=True)
  	#字符串是否要指定长度？
  	name = db.Column(db.String(20))
  	color = db.Column(db.String(20))
  
  	#在模型创建的时候指定表名
  	__teblename__ = '表名'   ==> 如果 没有指定和 类名一样 
  
  ```

  

  ![处理错误](C:\Users\msi\AppData\Roaming\Typora\typora-user-images\1568881056149.png)

  + 视图函数 views.py

  ```
  //创建表
  @blue.route('createTable')
  def createTable():
  	db.create_all()  ==> 创建表，方法 create_all
  	return '创建成功'
  ```

  + 增删改查

  ```
  //删除表
  @blue.route('dropTable')
  def dropTable():
  	db.drop_all()  ==> 删除表，方法 drop_all
  	return '表删除成功'
  
  //修改表名，在models.py中，
  	类中，指定表名
  	
  //通过模型添加数据
  @blue.route('/addanimal/')
  def addanimal():
  	a = Animal()
  	a.name = 'hen'
  	a.color = 'yellow'
  	
  	db.session.add(a)
  	db.session.commit()   ==> 必须哟啊提交
  	
  	return '添加成功'
  	
  //通过模型查询所有数据---  模型.query.all()
  @blue.route('/findall/')
  def findall():
  	animal_list = Animal.query.all()
  	
  	for animal in animal_list:
  		print(animal.name)
  	return '查询成功'
  ```

  

  