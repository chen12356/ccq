### 一、框架简介

Django----重量级框架 ---  核心代码多，就比如：安装一个包，就基本不用 其它包了。

Flask---轻量级框架 --- 自由灵活，只提供核心代码，都是借鉴其它框架的代码。flask也称‘micro frame work’使用简单的核心



### 二、flask 框架 

#### flask依赖库：

+ 模版引擎  ----  Jinja2
+ 工具集      ---   WSGI  --- 执行流程
+ 基于django 的签名模块   --- Itsdangerous

#### flask为啥受欢迎呢？

+ 有非常好的官方文档
+ 非常好的扩展机制，借鉴的很容易
+ 社区活跃度高（由于引用的较多，需要看第三方文档）
+ 微型框架、开发的空间大  --- 想用谁，就可以借鉴，灵活度非常高

#### BS/CS模式

现在**主流的 BS**模式 

​	  对于用户来说，bs容易满足用户，打开浏览器就可以使用。对于老板来说， 不必开发一个新客户端，比较省成本。对两者都方便。

概念：

BS ： B 浏览器   S 服务器    网络结构模式，把系统的实现功能的核心部分集中在服务器上

CS：  C 客户端   S 服务器  比较安全，在局域网上

**两者区别：(重要)**

| 对象 | 硬件环境                                                     | 客户端                                                       | 软件安装                   | 升级维护           | 安全性能                                                     |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------- | ------------------ | ------------------------------------------------------------ |
| C/S  | 通过局域网，小范围的网络环境。对客户的使用硬件环境要求比较高 | 对电脑的配置要求比较高                                       | 必须安装配置对应的 软件    | 比如一些补丁，升级 | 一般面向相对的固定用户群，信息安全控制能力比较高，一般比较高度机密的系统采用cs结构。更加注重流程，可以对权限的多层次校验 |
| B/S  | 建立在广域网上，不必要专门的网络环境。比较低，直接浏览器就可以执行 | 对电脑的配置要求比较低。大部分的、核心的功能都是在服务器上。 | 不需要，有个浏览器就可以了 | 不需要             | BS是建立在广域网上，对信息安全控制能力比较弱，因为面向的用都是不确定、不可知的。所有其适用的范围比CS广。 |

cookie缓存例子：
		在13年，北京有个品友公司， 说有中国90%的cookie浏览记录，但是没和央视合作，被央视曝光 。IE浏览器一样，微软是不会让你卸载的，它其实是需要用户的浏览记录，即cookie记录。这种记录对公司来说就是财富。

### 三、MVC/MTV

MVC：是一种**架构思想** （最高出现在桌面程序）

+ **目的**：将M和V的实现代码分离，从而使用同一程序可以使用不同的表现的形式（比如一批数据，用柱状图和饼图来表示），然而C层就是确保M和V的同步。一旦M层发生改变，V也应该同步更新。

+ **核心思想**：解耦合 （耦合：可以理解为联合度，关系度）
  + 解耦合： 降低M层和V层 的耦合性
  + 面向对象语言：低耦合、高内聚
+ **流程**： 用户请求 --> 控制器 --> 模型层 --> 取数据 --> 控制器 ---> 视图层

**MTV** ：python的架构思想 ，python的页面指的是 特普来

+ M 对应的 M    == >  模型层
+ T  对应的  V     ==>  视图层
+ V  对应的  C     ==>  控制层

模版 中可以 写 python 代码，模型 是不可以的。

### 四、 flask使用

#### 1、虚拟环境的创建

​	`sudo apt install  virtualenv `  ==> 下载虚拟环境

​	`mk 项目名`   ==> 创建项目名

​	``virtualenv  环境名`   ==> 在该项目下，创建虚拟环境

​	`source  env/bin/activate`   ==> 需要重载,，激活，才可进入虚拟环境

虚拟技术：虚拟机、虚拟环境、虚拟容器

**查看虚拟环境中的包**

​	`pip  freeze`  显示**非python自带的包**

​	`pip   list`   显示所有的包

**虚拟环境迁移**

​	`pip freeze > requirements.txt`   ==> **迁出**，写入的requirements.txt文件中

​	`pip install -r requirements.txt`   ==> **迁入**，一次性安装该文件的第三方包

#### 2、flask项目创建

+ 安装flask  

​	`pip install flask`   ==> 安装flask框架   ==>这是通过国外源下载

​	使用国内源安装：`pip install flask -i https://pypi.douban.com/simple`   --> 豆瓣源中安装 

+ **创建项目并启动服务器**
  + 利用专业版pycharm，左上角New-->点击flask --> 将配置环境选成 虚拟环境。
  + 利用社区版pycharm，和平常创建项目一样 --> 将配置环境设置为 虚拟环境 --> 注意还需要在项目下创建static和template文件夹。
  + 命令行创建，也是可以的，只是编写python代码不方便。

```
//flask基础结构

在文件夹中创建一个文件： helloflask.py
文件内容：
	from flask import Flask
	app = Flask(__name__)
	@app.route('/')  ==>设置路由，是用来访问的。
	def hello():
		return "hello"
	app.run()  ==> 启动项目
	
启动服务器（开发者服务器）：python 文件名.py  ==> 用python运行项目，会自动启动服务器
	取浏览器访问项目：127.0.0.1:5000      默认5000
```

+ **解决端口占用问题**

  + 在run方法中设置参数
  + 利用Manager--> 命令行启动参数
    + `python py文件名 runserver -p 8080 -h 0.0.0.0 -r`   建议带个-r

  ```
  // 1 在run方法中修改启动参数
  	在run函数中 参数host、port、debug等，都有默认值
    修改主机和端口号 可以在run函数中指定对应的参数
    	注意：host的值 是 字符串，port的值 是int或者字符串，
    		但是在pymysql模块中，port的值 必须 整型。
  	如：app.run(port=8888,host='0.0.0.0')
  
  // 2 命令行参数
  	安装：pip install flask-script
  	初始化：文件名改为manager.py
  		   manager = Manager(app=app)  ==> app交给manager管理
  		   manager.run()
  runserver 就是开发者服务器（low，高并发就不行了）	   
    启动：python manager.py runserver -p 端口号
    如果想让其他人也访问： 加个参数 -h
    		python manager.py runserver -p 端口号 -h '0.0.0.0'
    
    问题：代码更新了，逻辑改了，需要重启服务器才能使用，如何解决不用重启？
    		python manager.py runserver -r  ==> 加个参数-r
  注意：如果修改的是python代码，那么服务器会自动重启，静态文件修改完了是不会重启的如css，js，html（不是模版）
  ```

  **扩展：PIN码**

  ​	runserver -d    ==> 会有一个pin码，开机重启都需要输入pin码，比如sim卡就是设置pin码。在run方法中，参数debug和该-d是一样的意思。

开发环境-测试环境-演示环境-线上环境

### 五、视图函数 

+ 定义视图函数 （需要设置路由@app.route('请求路径’)）

```
如果路由格式：/index/ 那么请求资源的路径：127.0.0.1:5000/index或者 127.0.0.1:5000/index/   后面的 / 不写会补全

@app.route('/index/')  ==> 设置路由
def foo():
	return 'xxxx'

//路由设置了/index1  ==> 如果请求路径后面加了 / 会报错404 ，没有/不可以加 /
@app.route('/index1')
def index1():
	return "sss"
```

+ 视图函数返回值
  **返回字符串、返回页面、添加静态文件(css、js、img、视频等)**

```
//返回字符串
@app.route('/testreturn/')
def testreturn():
	return '1'
//注意，返回值必须是字符串、字典、元组、response对象（不可以是整数）

//返回页面,需要导入flask中的render_template方法
@app.route('/testreturn1/')
	return render_template('testreturn1.html')   ==> 该方法返回的是字符串
						 注意：该html文件是在template文件中
						 
比如：执行完视图函数，我需要跳转到页面， 
需要：在社区版需要创建：static、templates 两个文件夹

在templates写html文件：
 比如有个：  testreturn1.html 
 
添加静态文件，在static文件夹下
比如：testreturn1.css

需要在templates中的html需要用link标签来导入css
	<link rel='stylesheet' href='/static/testreturn1.css'>  ==>需要注意rel,
```

### 六、封装

**`第一次封装和蓝图`完整的代码练习在项目`flask3`中**

每个程序里很多的功能，比如一个商品有：首页、动态、购物车、我的 四个大模块。那么我们就可以  封装 这些模块。 让 架构  更加清晰

封装的次数 ==> 大数是三次， 一次比一次麻烦

```
1、创建一个名为App的 python Package 文件。 里面默认：__init__.py
   App存放：static、templates、views.py、models.py
```

**模型**：对应的数据，（如orm，数据库 中 表的字段 与 类对象属性一一对应，这就是模型，提到某一物会联想到另一物）

比如：每个模块肯定都有静态文件、模版、页面，模型：数据模型和表一一对应, 所以每个App都要有的文件。

那么里面的文件如何写呢？

​	把manager.py的关于视图的部分，移动到views.py 里面。因为视图函数拿到views.py中，现在找不到了路由，那么利用 蓝图 解决

```
在views.py中
	from flask import Blueprint,render_template
	blue = Blueprint('blue',__name__)
	@blue.route('/')
	def test():
		return render_template('xxx.html')
在manager.py文件中
	from flask import Flask
	from flask_script import Manager
	from App.views import blue
	app = Flask(__name__)
	app.register_blueprint(buleprint=blue)  # 需要注册蓝图
	manager = Manager(app=app)
	
	if __name__=="__main__":
		manager.run()
上面过程就是将主程序中视图的代码，封装在了 views.py文件中。
```

循环导入：指的是两个文件A、B，A导入B，B导入到A ，在python是不行的，因为在底层是由线程挂起的。比如：你等着我，我等着你，两者都等不到



### 七、蓝图

​	一种规划，规划路由，可以让主程序的代码与封装完的views视图建立关系。

​	安装：`pip install flask-blueprint`  或者 直接导入`from flask import Blueprint`

​	初始化：`blue = Blueprint('蓝图名',__name__)`

​	注册蓝图：`app.register_buleprint(blueprint=blue) `

**注意**：蓝图的对象的创建必须在 views.py里面。

如何App中的views.py和manager.py 建立关系：

```
1、首先在App中views.py中创建蓝图对象。
需要注意：Blueprint是由flask导入的。
	from flask import Blueprint
	blue = Blueprint('blue',__name__) ==> 创建了名为blue的蓝图对象
	@blue.route('/text/')   ==> 利用蓝图对象来设置路由
	def test():
		return "hello" 
2、在manager.py文件中需要 注册蓝图对象，这样两者才会关联到一起
   先创建 app = Flask(__name__)
   app.register_blueprint(blueprint=blue)  ==>该blue是由views.py导入过来的
   manager = Manager(app=app)
   if __name__ == '__main__':
  		manager.run()
```

### 八、Flask请求流程

```
浏览器发起请求 ==> 到路由route ==> 从而进入路由中指定的视图函数 ==> 视图函数和models交互 ==> 模型返回数据给视图函数 ==> 视图函数渲染模版(template) 用render_template ==>返回给浏览器，展示页面. 
```

flask和Django最核心：**路由的分发(flask做的)**，根据请求的路径，返回指定的视图函数。

![1568771425079](C:\Users\msi\AppData\Roaming\Typora\typora-user-images\1568771425079.png)

### 九、路由参数

从客户端或者浏览器 ===> 服务器参数

+ **没有变量名，没有值，没有问号？**

  + 如：`http://www.baidu.com/s/1/`

+ 基本结构

  + ```
    路由参数格式：/请求资源路径/<变量>   ==>利用 <> 括起来
    请求访问路径:  127.0.0.1:5000/testRoute/1  ==> 此时1 就是传递的参数
    
    @blue.route('/testRoute/<id>/')
    def test(id)  ==> 视图函数需要与路由参数一致。
    	print(type(id))  ==>路由参数传给视图函数，是字符串类型
    	return 'testRoute'
    ```

  + 路由参数类型

    + 字符串（默认情况下）#

      + ```
        //string 字符串
        //遇到 / 斜杆  代表着结束。
        @blue.route('/testRoute1/<string:name>')
        def test1(name):
        	return 'test'
        ```

      + 

    + path 

      + ```
        //path也是一个字符串，
        //会把 / 斜杆 当做字符来处理。
        @blue.route('/testRoute2/<path:name>/')
        def test2(name):
        	return 'test'
        ```

    + int

      + ```
        @blue.route('/testRoute3/<int:money>/')
        def test3(money):
        	return 'xxx'
        ```

    + float

      + ```
        @blue.route('/testRoute4/<float:price>/')
        def test4(price):
        	return 'xxx'
        ```

    + uuid

      + ```
        //生成uuid向
        @blue.route('/testuuid/')
        def test():
        	uid = uuid.uuid4()
        	print(uid)
        	return 'xxx'
        //利用uuid做路由参数
        @blue.route('/testRoute5/<uuid:uid>/')
        def test5(uid):
        	return 'xxx'
        ```

    + any

      + ```
        //any()  ==> 参数可以是 () 内任意一个 
        @blue.route('/testRoute6/<any(a,b):p>/')
        def test6(p):
        	return 'xxx'
        访问：
        127.0.0.1:5000/testRoute6/a/
        127.0.0.1:5000/testRoute6/b/  ==> a,b都可以的
        ```

+ 另一种参数：请求资源路径参数，带?号的

  + 也即是平常浏览页面的路径

### 十、模拟请求方式 postman   （pycharm也有）

请求方式：又称http方法

+ get  --- 获取
+ post  --- 添加
+ delete  --- 删除
+ put ---修改全部属性
+ patch --- 修改部分属性

需求：执行一个视图函数，跳转到一个模版 login.html，在模版中输入用户名，然后点击登录，点击之后 显示 欢迎光临红浪漫。

```login
@blue.route('/toLogin/')
def toLogin():
	return render_template('login.html')

//路由默认只支持 get、head、options ； 不支持post、delete
// 如何可以使用 post、delete、put、patch,怎么办？

// 解决：在route方法中添加一个methods 参数-- methods=[]
// methods的列表参数的元素 大小写都可以的。

@blue.route('/login/',methods=['post','delete'])
def login():
	return '欢迎光临'
	
```

模版：

```
login.html
…………
<from action="/view中的路由/" method="post">
	<input type="submit" >
```

模拟请求工具：postman

默认支持：get、head、options，想支持某一种请求格式，需要手动指定

```
@blue.route('/testPostman/',methods=['psot','get','put'])
def testPostman():
	return '你的梦想是否只是说说而已'
```

状态码

```
200  --- 成功   为啥200 ==> 接收到全部数据，并且没有数据丢失，这两层判断才是200
301  --- 重定向
302  --- 永久重定向
403  --- 防跨站攻击
404  --- 网页没找到
405  --- 请求方式不允许
500  --- 服务器错误（业务逻辑出错）

```

### 十一、反向解析

+ 获取请求资源路径

```
@blue.route('/testReverse/')
def reverse():
	return 'reverse'
	
@blue.route('/testReverse1/')
def reverse1():
	#获取请求资源路径
	
	#反向解析语法： url_for('蓝图名字.方法名字',方法参数=值)   ==>方法有参数的话，传递关键字参数
	s=url_for('blue.reverse1')  ==> 得到该方法的资源路径
	print(s)  ==> /testReverse1/
	return 'reverse'
```

+ 应用场景
  + 重定向到index请求中 ==> redirect('/index/')
    + 尽量不要使用硬编码(代码写死)
    + 那么解决：把重定向和反向解析结合 ==> redirect(url_for('blue.index'))
  + 在页面中不要写硬编码 ==> 如 from action=‘/login/’
    + 利用反向解析： from  action = "url_for('blue.login')"

### web后端开发

```
概要分析 ==> 知道你要干啥
详细设计 ==> 具体怎么做 
编码   ==>
测试   ==>  黑盒，白盒等
申请一个IP  ==> 去公安局备案（被封）
租赁服务区  ==> 非常昂贵，比如阿里云服务器原先占了90%，为了10%,挖了王坚，创建了阿里云
部署

域名和iP是  一一对应，ip不好记，记域名

比如：一个浏览器发生一个 请求 ，先是DNS服务器进行域名解析，返回一个IP，然后浏览器得到IP向服务器访问带着请求报文。服务器会发送一个响应response。
	访问服务器：request 有请求报文（请求头。请求体，请求行）
	服务器响应：response  响应报文
	
如何把项目放到服务器上： （接口：如usb接口都一样，符合同一的规范称为接口）
	wsgi服务器网关接口（大多数框架都有这个接口，符合WIGI接口，会把项目自动的部署到服务器上）
```

![1568690673048](C:\Users\msi\AppData\Roaming\Typora\typora-user-images\1568690673048.png)