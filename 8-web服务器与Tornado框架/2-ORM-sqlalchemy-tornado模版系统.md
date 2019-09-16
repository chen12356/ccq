### 一、ORM：对象关系映射

一套通用的系统，作用：在编程中把面向对象的概念跟数据库中的表的概念对应起来。

简单例子：一张表中多个字段，也就是多个列，然后在定一个类，把这张表的字段名用作这个类的属性，并且是类属性，直接可以通过类来调用这些属性，也就是调用这些字段。每个类的实例就是相当于这张表的每一行。。

**python中常用的ORM**：Django-ORM（比较完整的一套ORM）、SQLAlchemy、Peewee（新出的，更加轻量级，速度也比较快，日常使用没有问题）

ORM 优点：

+ 数据模型都在一个地方定义，更加容易维护和修改更新。

+ ORM有现成的工具，很多功能都可以自己完成，比如数据预处理，事务等等

+ 迫使你使用MVC架构，ORM就是天然的Model层 ，使的代码更加的清晰。

  

+ 性能比较普通，不算太差，也不算太好，如果达不到自己系统的满足的需求那么也可以自己写sql语句。

**如果自己定义一个ORM系统你会怎么做？**

​	先写好一个基类，表的一些字段，定义一些增删改查方法。比如简单的create函数，不管怎样必须写个sql语句，所有create函数的参数，需要接受一些参数，比如

```
//比如类中的某个方法
def create(self,*args):
	sql_template = 'insert into %s values (%s……)'%(self.id,……self.sex，……)
	pymysql……execute(sql_template)
	#上面是拼一个sql的语句的模版
本质上：对sql语句进行封装
```

### 二、SQLAlchemy 示例

对SQL进行一些提炼的意思，技术也比较成熟，比如一些分布分表。2010年一些公司就开始用这个库，集成太多太多的功能，但是有时候显得比较臃肿

本质上：通过类来操作数据库。

首先先导入 `pip install sqlalchemy`

```
import datetime
//engine连接的引擎，与数据的连接
from sqlalchemy import create_engine
//持续的连接该过程，称为会话，用来创建会话的函数
from sqlalchemy.orm import sessionmaker
//Colum(col)列，导入满足的类型
from sqlalchemy import Colum,String,Integer,Float,Date
//特殊的函数，用来创建创建整体数据模型的基类
from sqlalchemy.ext.declarative import declarative_base

#建立连接与数据库的连接
#初始化连接
#格式：'数据库类型+数据库驱动名称://用户名:密码@机器地址:端口号/数据库名'
//mysql+pymysql 两者的对接
engine = create_engine('mysql+pymysql://ccq:123@127.0.0.1:3306/ccq')

 #创建模型的基础类,咱们对数据的所有操作都是基于基类。
 #注意Base是一个；类，可用通过其创建一些实例
Base = daclarative_base(bind=engine) #绑定上面的连接

#创建Session类，会话
 #注意Session是一个；类，可用通过其创建一些实例
Session = sessionmaker(bind=engine)

class User(Base): ==>继承了Base类
	'''定义User对象
	类属性，不需要实例属性，直接用类来取数据,,里面都是表的结构
	'''
	__tablename__ = ''  #表名 =>这是sqlalchemy自己定义的。
	#表的结构，每个字段都是 一个列，里面的类型
	id = Colum(Integer,primary_key=True)
	name = Colum(String(20),unique=True)
	birthday = Column(Date,default=datetime.date(1990.1.1))
	money = Colum(Float,default=0.0)
	
//metadata 元数据（表本身结构，字段一些信息）表指的是__tablename__
Base.metadata.create_all(checkfirst=True)   #创建表结构

//定义与数据库的会话，持续的连接，你的所有操作记录在数据库中
session = Session()

#定义了一些对象，直接用对象，该表的一些信息，对应数据库的一行数据
bob = User(name='bob',birthday=datetime.date(1996,10,23),monry=123456)
tom = User(name='tom',birthday=datetime.date(1992,1,3),monry=1236)
lucy = User(name='lucy',birthday=datetime.date(2000,8,28),monry=3456)
……

#增加数据
//session.add(bob) ==>添加
session.add_all([bob,tom,lucy])  #里面传递的是一个列表，列表的元素是实例对象，

//session会话需要提交，才可以生效
session.commit()

#删除数据
session.delete(lucy)
session.commit()

#改数据
tom.money = 121212
session.commit()

#查数据
#session.query(类) 
q = session.query(User)
#有两个查询函数，filter、filter_by
//得到id为5得那个对象
result = q.filter(User.id==5) ==>得到的result是个User对象。

//得到id大于5的那个对象
#result = q.filter(User.id>=5) ==>此时result是是个迭代对象，用for循环输出
#result = q.filter(User.id>=5).frist  ==>得到第一条

//根据ID号，对出生日期排序
//result = q.filter(User.id>2).order_by('birthday')
//for u in result:
//		print(u.name……)


//取指定条数，取三个，从第四个开始取
//result = q.limit(3).offset(4)

//计数
//result = q.filter(User.i>2).count   ==>得到id大于2的个数


//一次查询，并且更新,后面直接更跟update,参数1，更新数据，字典形式，
q.filter(User.id==1).update({'money':9999},synchronize_session=false)
sesssion.commit()

//简单的字符串凭借,指定的字段
q.filter(User.id==1).update({'money':9999 + User.money},synchronize_session=False)
sesssion.commit()


//filter_by 和filter的条件写法不一样。
//q.filter_by(id=1).one().name
//比如：city为上海的
result = q.filter_by(city='上海') 

//查看在不在,exists()
result = q.filter_by(name='李四').exists()
session.query(result).scalar  ==>结果为True和False
//这里判断存不在存在：涉及到了orm中懒加载/惰性加载  ==> 有些惰性求值思想的体现

惰性求值中：
	这里的filter和filter_by 的语句，只是仅仅的一条语句，并没有和数据库进行通信，只是得到的一个query对象而已。如何真正的需要得到值了那么就会和数据库通信。这就是惰性取值的一些过程。
```

##### 惰性求值

### 三、tornado模版系统

模版系统：为了更快捷、更方便的生产大量的页面而设计的一套程序。

借助模版系统：可以先写好网页的大概框架。然后预留好可变数据的位置，最后将我们需要的数据，按照既定的规则拼到模版里面，用render 渲染出完整的页面（把原先的write改成render）

#### 1、模版配置

```
模版的位置(放的是网页模版)
tempate_path='templates'
静态文件位置（放置静态文件，照片，视频等 ）
static_path = 'static'

两者的位置：与当前的执行的py文件在同一文件夹，且同级 


在当前py文件中
class Mainheadler(tornado.web.RequestHeadler)
	def get(self):
		//定义参数来传值
		abc = self.get_argument('arg','默认') ==>页面上接收了 arg对应的内容
		name = self.argument('name','Admin')
		sex = self.get_argument('sex','保密')
		menu = ['rou’,'dj','dd']  ==>一个列表，下面循环处理
		self.render('index.html',data='你好')  ==>render 渲染了该页面，找到模版位置里面的index.html
```

**配置模版和静态文件的位置：**

```
`__file__` ==> 指的是当前文件的文件名

导入os模块

print(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.abs(__file__) ==>这是得到该项目的文件夹。绝对路径
template_dir = os.path.join(base_dir,'templates')
static_dir = os.path.join(base_dir,'static_dir')
就可以把将上面的两个模版位置和静态文件位置替换成绝对路径。（比较建议这么做）

需要在make_app函数里面给APPlication中传参数。
def make_app():
	result = [(r"/",Mainheadler )]
	return tornado.web.APPlication(result,template_path="template_dir",static_path="static_dir")
里面在APPlication中除了传递列表参数外，还需要传个模版位置和静态文件的位置
```

#### 2、定义模版

在templates文件（定义的模版位置）中内容，编写模版，比如下面的index.html

+ index.html文件内容

  + 变量、if语句、for循环语句
  + **注意写法的格式**：语句的话需要：{% 语句 %}，变量直接：{{变量名}}，注意区别。
    在语句的结束，还需要 {% end %} 标志结束

  ```
  <!DOCTYPE html>
  <html>
  	<head>
  	<head>
  	<body>
  		<p>{{data}}</p>   ==>此时这个data的指的上面的render里面的参数data对应的。，在{{}}还可以写一些运算
  		{% if sex == '男 %}         ==>if判断语句
  			<p>你好 {{name}} </p>
  		{% elif sex == '女' %}
  			<p>你好 {{name}}</p>
  		{% else %}
  			<p>你好 {{name}}</p>
  		{% end %}
  		
  		<hr>
  			今天菜单：
  			<ol>
  				{% for item in menu %}  ==>  for循环语句
  				<li>{{item}}</li>   ==>注意没用% % 
  				{% end %}
  			</ol>
  		</hr>
  		
  	</body>
  </html>
  ```

  还可以进行简单运算：

  ```
  
       <p>{{3 * 2}}</p>  ==>进行运算，需要创两个参数
       <p>{{ [i for i in range(10)] }}</p>  ==>做一些循环
  ```

  **注意：strong标签具有强调的作用，优先级较高**

#### 3、模版的继承

也是存在 模版位置里面的html

需要注意：

+ 继承的关键字 extends 
+ a.html文件继承b.html，只要将父类中的b.html模版中需要插入数据的一些占位的位置（比如：{% block  名称 %} ……{% end %}）。那么需要在a.html中对这些位置进行插入数据，标签等操作。

比如下面的例子：

+ model.html  --**基础模版**

```
//基础模版
<!DOCTYPE html>
<html>
	<head>
		<title>aaaa</title>
		<style>
			body {
				width:900px;
				margin:0 auto;
			}
			.content {
				float:left;
				width:700px;
			}
            .sidebar{
            	float:left;
            	width:200px;
            }
				
				
		</style>
	<head>
	<body>
		<!-- 导航区 -->
		<div class="navbar">
			<a href="#">要闻</a>
			<a href="#">娱乐</a>
			<a href="#">财经</a>
			<a href="#">体育</a>
			<a href="#">时尚</a>
		</div>
		<h1></h1>
		<hr />
		<p></p>
		<!-- 内容区 -->
		<div class="content">
			{% block container%} {%end%}  ==>中间是插入的内容，其中block是关键字，后面的是 起的名字

		</div>
		<!-- 边栏区 -->
		<div class='sidebar'>
			<ul>
				<li><a href="#">砂浆佛自己撒地方 </a></li>
				<li><a href="#">砂浆佛自己撒地方 </a></li>
				<li><a href="#">砂浆佛自己撒地方 </a></li>
				<li><a href="#">砂浆佛自己撒地方 </a></li>
				<li><a href="#">砂浆佛自己撒地方 </a></li>
			</ul>
		</div>
		
	</body>
</html>

```

现在继承model.html的模版

article.html

```
{% extends 'model.html' %}  ==> 继承了model.html模版

{% block container %}   ==>找到model.html中的需要插入数据的内容的小版块
<h1>{{ title }}
<p>
	{{ content }}
</p>
{% end %}   ==>该小版块的结尾， 中间的标签是动态插入到父模版里指定的位置

//对于这个页面来说，传递两个参数，
// 只需要传数据，模版是继承的，直接把当前的标签插入到父类模版指定模块里。
```

#### 静态文件

 在html中，比如我需要传图片  ，，src 属性中，路径前面需要加 /static/

```
    <img src="/static/静态文件目录下的相对路径">
```

/static/  静态文件的固定的 url 前缀

img/coder.jpg    在本地的静态文件位置中，对应的文件的相对路径

/static/img/coder.jpg   两者整合==>这是在网页上看到的图片的路径。

​	其中 /static/ 就是原先传入 Application 中的静态位置。利用这个关键字来/static/ 是会自动在内部把这两端路径拼接成了绝对路径。这样就访问到该图片的位置。