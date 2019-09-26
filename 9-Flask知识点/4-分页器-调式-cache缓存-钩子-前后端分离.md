### 1、分页器

练习小项目中的应用中有完整的

```
//视图函数中：
	模型.query.paginate()  ==> 方法的返回值类型是Pagination
 	其中：page ==> 页数
 		per_page ==> 一页有多少条数据
//在模版中
pagination 对象的方法
	items 遍历 对象
	pages（获取总页数）
	prev_num （上一页的页码）
	has_prev （是否有上一页）
	next_num （下一页的页码）
	has_next （是否有下一页）
	iter_pages （当前的页码）
```

+ 例子	

  ```
  // 视图函数
  @blue.route('/userList/',methods=['GET','POST'])
  def userList():
      page = int(request.args.get('page',1)) ==>第一次添加，默认第一页
      per_page = int(request.args.get('per_page',5)) ==>每页的数据量数
      #创建一个Pagination对象，然后传给了模版
      info_list = Info.query.paginate(page=page,per_page=per_page)
      return render_template('userList.html',info_list= info_list)
  
  
  //模版中使用Pagination对象
  
  	{% if info_list.has_prev %}
  		<a href="{{url_for('blue.userList')}}?page={{info_list.prev_num}}" style="margin-left:300px">上一页</a>
  		{% else %}
  			<a href="#" style="margin-left:300px">上一页</a>
  	{% endif %}
  
  	{% for p in info_list.iter_pages() %}
  		<a href="{{url_for('blue.userList')}}?page={{ p }}">{{ p }}</a>
  	{% endfor %}
  
  	{% if info_list.has_next %}
  		<a href="{{ url_for('blue.userList')}}?page={{ info_list.next_num }}">下一页</a>
  		{% else %}
  			<a href="#">下一页</a>
  	{% endif %}
  	<p>
  
  ```

  

### 2、flask-bootstrap

```
插件安装：pip install flask-bootstrap

ext文件中初始化： Bootstrap(app=app)


```

### 3、flask-debugtoolbar

```
辅助调试插件

1、安装
	pip install flask-debugtoolbar
2、初始化 
	第三方包，均方在ext文件里
	app.debug = True  ==> 最新版本需要
	debugtoolbar = DebugToolbarExtension()
	debugtoolbar.init_app(app=app)

```

### 4、flask-cache 缓存  	

**4-7 部分完整的代码在项目 `day06flask`中**

```
1、为什么缓存：
	缓存优化加载
	减少数据库的IO操作  ---> 把将经常用的数据放到缓存中，这样就不用操作数据库。
	
2、数据库缓存、样式缓存(比如css文件后缀map)对部分浏览器支持。相同的样式我缓存在浏览器上，下次访问，直接使用该缓存。

3、实现方案  ---   也就是缓存的数据 存放的位置
	数据库 --- 不建议
	文件中 --- 少量数据可以，但也不建议
	内存   --- 关机就没，不建议
	内存中数据库  --- redis (最优策略)
	
4、实现流程
	1-从路由函数进入程序
	2-路由函数到视图函数
	3-视图函数去缓存中查找
	4-如果缓存中找到，直接返回数据
	5-如果缓存中未找到，直接去数据库中查找
	6-数据库查到的数据，除非存放到缓存中
	7-返回页面
	
5使用：
  安装 -->	pip install flask-cache
  初识化 --> 指定缓存方案(保存的位置)
  	ext文件配置中：
  		#如果cache在方法中，在其它文件中是到不了，需要写炒成全局变量
  		cache = Cache(config={'CACHE_TYPE':'redis'})
  		
  		#如果包
  		#底层源码我们需要修改，因为这个错官方没有修改
  		解决方法：
  			1、打开site-package
  			2、flask-cache下的jinjia2ext.py文件
  			3、修改from flask.ext.cache import …… 为 from flask_chche import··
  			
  		cache.init_app(app=app)
  		#此时配置完成了
  		
    view.py视图中使用：
    
    @blue.route('/helloCache/')  #视图放上下对页面没影响的，对cache就有影响
    #1、装饰器缓存
    @cache.cached(timeout=30)#等待的时间30s后在执行，要想让cache起作用，必须放视图路由的下面
    def helloCache():
    	print('2003年的第一场雪')
    	return 'helloCache'
#上面这种：利用cache装饰器， 设置timeout,每次点击生效时间是30s,否则在中间的时间中点击时无效的。 	
  
#下面这种：将数据存入到cache缓存中，这里放到的是redis中，下次访问查询的时候，先找cache缓存，如果没有，查数据库，然后存入cache缓存中，下一次就不用访问数据库了
   	#2、第二种应用场景
   	@blue.route('/testCache/')
   	def testCache():
   	# 如果第一次访问，那么显示 欢迎光临
   	#	如果第二次访问，那么显示  小爬虫快走开
   	#如何知道你是第二次访问：利用request.remote_addr()
   	
   		value = cache.get('ip')
    	if value:  ==> 在缓存中找到，返回一句话
    		return '小爬虫，快走开'
    	#否则是第一次访问，那么存入缓存中
    	ip = request.remote_addr
    	cache.set('ip',ip)
    	return '欢迎光临'
```

### 5、钩子

```
#原理：在纵向开发的基础上支持横向开发，如同嫁接；在代码的执行的过程中，添加另一个方法的执行
#aop ---> 面向切面编程
#现再下面的操作，都要连接数据库，代码有点冗余了。如果封装函数，需要的时候调用(该方法不优秀)
#利用：钩子
#好处：减少代码冗余，解耦合

#钩子
@blue.before_request   ==> 请求之前做的操作
def beforeRequest():
	print('连接数据库----')
#此时下面的方法，并不用连接数据库了，也可以使用，解耦合

#增
@blue.route('/add/')
def add():
	#print('连接数据库')
	return 'add'
#删
@blue.route('/delete/')
def delete():
	#print('连接数据库')
	return 'add'
#改
@blue.route('/update/')
def update():
	#print('连接数据库')
	return 'add'
#查
@blue.route('/find/')
def find():
	#print('连接数据库')
	return 'add'


```

### 6、四大内置对象

```
1、request
2、session
3、config
4、g
```

+ `config` ==> 有两种情况使用(python中和页面中用法不同)

  ```
  //页面中使用 testTemConfig.html
  ……
  <body>
  	今天天气很好
  	
  	{% for in config %}
  		{{ c }}   ==> 这个c是config对象里面的值，不需要创建config
  	{% endfor %}
  	
  </body>
  
  @blue.route('/testConfig/')
  def testConfig():
  	return render_template('testConfig.html')
  	
  //python代码中
  @blue.route('/pythonConfig/')
  def pythonConfig():
  	for c in current_app.config:
  		print(c)
  ```

+ `g`

  ```
  @blue.route('/g/')
  def g():
  	g.ip = request.remote_addr
  	return 'g'
  
  @blue.route('/testG/')
  def testG():
  	print(g.ip)  #如何得到上面获取的ip
  	return 'testG'
  注意：需要先生成g，后面才可以使用，对于上面的代码的操作，先执行g，生成g.ip,然后testG才可以运行。
  ```

### 7、路径

```
//__init__文件中
import os
#先找到模版和静态资源的绝对路径，然后传给app
#处理template与static问题，原先是在App文件下，现在迁移到项目目录下
templates = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'templates')
static = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'static')


def create_app(env_name):
    app = Flask(__name__,template_folder=templates,static_folder=static)
    app.config.from_object(settings.ENV_NAME.get(env_name))

    init_app(app)
    return app

一个项目中有很多app，那么模版和静态文件一定要项目的下，那么多个App都可以继承。因为模版可以继承


//views.py
#处理
# templates 和 static的路径问题
#把模板和静态资源文件夹放到项目的目录下，因为一个项目不止1个App，这样可以让多个App继承模板
@blue.route('/path/')
def path():
    return render_template('path.html')
```

### 8、前后端分离

​	**完整代码在`day06flask2`中**

```
REST  ： 一种软件架构风格，并不是标准。主要用于客户端和服务器的交互类的软件
表示===> 表征性状态转移。
作者：Roy Thomas Fielding博士，是http协议1.0和1.1主要设计者。Apache软件的作者之一，apache基金会的第一任主席。 
```

+ 前端和后端需要**用json**来进行交互

```
//视图函数返回Json文件
@blue.route('/testJson/')
def testJson():
	data = {
		'msg':'ok',
		'status':200
	}
	#强制类型转换
	data = jsonify(data) ==>返回Response对象
	print(type(data))
	return data 
```

+ **前后端分离---查询**

  ```
  注意：前后端分离是不可以直接传输对象的。所以在模型类中定义一个方法获取数据。如定义to_dict方法
  def to_dict(self):
  	return {'id':self.id,'name':self.name}
  
  
  @blue.route('/toGetAnimal/')
  def toGetAnimal():
      return render_template('getAnimal.html')
  //查询
  @blue.route('/getAnimal/')
  def getAnimal():
  	#animal = Animal.query.first() 单个对象
  	
  	animal_list = Animal.query.all()  #多个对象
  	animals = []
  	for animal in animal_list: #遍历basequery对象
  		animals.append(animal.to_dict())
  		
  	data = {
  		'msg':'ok',
  		'status':200,
  		'animal':animals
  	}
      return jsonify(data)
  	
  @blue.route('/toRegister/')
  def toRegister():
      return render_template('register.html')
  	
  模版getAnimal.html
  	<script  先引入></script>
  	<script>
  		$(function(){
  			$('button').click(function(){
  				//getJson的参数格式， url 请求资源路径
  									data  请求参数dic类型
  									function(data){}返回值
  				//getJSON能做：发送请求，并且接收响应数据，并接收到的数据 在页面中进行渲染
  				$.getJSON('getAnimal',
  							//视图函数返回的内容
  							function(data){
  								var animals = data['animals'];
  								var $ul = $('ul');
  								for(var i=0;i<animals.length;i++){
  								//创建li标签
  								var $li = $('<li></li>');
  								//标签中的内容
  								$li.html(animals[i].name)
  								//往列表中添加元素
  								$ul.append($li);
  								}
  							})
  			})
  		});
  	</script>
  	
  <body>
  	<button>点我</button>
  	<ul></ul>
  </body>
  
  ```

  接口开发：

  ```
  比如前端需要：
  	url 请求资源路径
  	data  请求参数dic类型
  	function(data){}返回值
  ```

  补充jquery：

  ```
  封装了js的一个框架
  入口： $(function(){
  
  });
  	事件驱动：
  		click
  		blur
  		change
  		keyup
  	$('#name').click(function(){
  		点击后的功能
  	})
  原生的js：
  	onclick = aaa();
  	
  	function aaa(){
  	
  	}
  
  ```

+ **前后分离之 添加**

  + 注意前后端分离没有表单

  ```
  @blue.route('/toRegister/')
  def toRegister():
  	return render_template('')
  	
  @blue.route('/register/')
  def register():
  	name = request.args.get('name')
  	animal = Animal()
  	animal.name = name
  	db.session.add(animal)
  	db.session.commit()
  	data = {
  		'msg':'ok',
  		'status':200,
  		'animal':animal.to_dict()
  	}
  	print(data.get('animal'))
  	return jsonify(data)
  	
  @blue.route('/index/')
  def index():
  	return '精神'
  
  
  //模版 Register.html
  	
  	<script  先引入></script>
  	<script>
  		$(function(){
  			$('button').click(function(){
  				var $name = $('#name').val()
  				//发送给视图函数
  				$.get('/Register/',
  						{'name':$name},
  						function(data){
  							//跳转页面，两种方式,参数是不会开创新窗口
  							window.open('/index/',target='_self');
  							//第二种,在当前页面中跳转
  							window.location.href='/index/'
  						}
  				)
  			});
  	
  	</script>
  <body>
  	name:<input type="text" id="name">
  	<button>提交</button>
  </body>
  
  ```

+ 修改

  ```
  一般是用
  put请求  ==> 修改全部
  path请求   ==> 修改部分
  请求利用邮差来实现
  
  @blue.route('/testPut/',methons=['put','patch'])
  def testPut():
  	animal = Animal.query.first()
  	animal.name = 'python'
  	db.session.add(animal)
  	db.session.commit()
  	data = {
  		'msg':'ok',
  		'status':200,
  		'animal':Animal.to_dict()
  	}
  	return jsonify(data)
   
  ```

+ 删除

  ```
  delete 请求
  
  @blue.route('/delete/',methons=['delete'])
  def delete():
  	animal = Animal.query.first()
  	
  	db.session.delete(animal)  #删除
  	db.session.commit()
  	data = {
  		'msg':'ok',
  		'status':200,
  		'animal':animal.to_dict
  	}
  	return jsonify(data)
  ```

+ 整合--> 封装

  + 注意：判断请求的方式的时候，请求方式必须是大写
  
    ```
    @blue.route('/animal/',methods = ['get','post','put','patch','delete'])
    def animal():
    #简单的封装，根据添加条件判断不同请求，返回对应的data，
        if request.method == 'GET':
            data = {
                'msg': 'get',
                'status': 200
            }
            return jsonify(data)
    
        elif request.method == 'POST':
            data = {
                'msg': 'post',
                'status': 200
            }
            return jsonify(data)
    
        elif request.method == 'PUT':
            data = {
                'msg': 'put',
                'status': 200
            }
            return jsonify(data)
    
        elif request.method == 'PATCH':
            data = {
                'msg': 'patch',
                'status': 200
            }
            return jsonify(data)
    
        elif request.method == 'DELETE':
            data = {
                'msg': 'delete',
                'status': 200
            }
            return jsonify(data)
    
    
    ```
  
  上面的是原生的前后端分离，需要判断请求条件

### 9、前后端分离的封装---**flask-restful**

+ **此标题的代码在 `day06flask-restful-FZ`项目里面**

避免了原生的两大弊端，1-返回数据的序列化问题，不用在模型中写方法，2-不需要判断请求方式

```
安装 pip install flask-restful

初始化：和视图函数没啥关系，不使用蓝图了
	首先 在App下创建urls.py 文件
		api = Api() 创建api对象
		
		def init_urls(app):
			api.init_app(app=app)  初始化
		
		api.add_resource(CatResource,'/cat/')  #执行的路由
    
    在App中创建apis文件夹
    	并在apis文件夹下创建 CatApis.py
    				该类是继承了Resource，是给urls调用的，api.add_
    		class CatResource(Resource):
    			 def get(self):
                       return {"msg": "ok"}

                 def post(self):
                       return {"msg": "create success"}
    			  ………………put、patch、delete请求
	 然后在__init__文件中调用 init_urls方法。

		
```

+ #### 定义结构化输出  --> marshal

  + 可以返回对象、返回列表详细见下面例子

  + 上面的基础上，在定义一个 Cat1Apis.py

    ```
    同样：class Cat1Re……
    
    		r1Fileds = {
    			'msg':fields.String,  需要导入
    			'status':fields.Integer,
    			'eroor':fields.String(default='false') 设定默认值
    			
    		}
    		
            #需要一个装饰器,需导入
    		@marshal_with(r1Fields)
    		def get(self)
    结构的数据多，返回的数据少   =>返回的少的，那么给默认值
    								如果是Ingeter类型默认为0
    								如果是String类型默认为null
    ……      少，         多   =>没有，自动过滤结构化中没有的
    如果两者相等，那么正常输出。
    
    fields后面的类型 可以加(), 可以不加()
    
    ```

  + fields 的类型约束

    + 1-arrribute(指定连接的)

  + marshal的第二种用法
  
    ```
    //新建一个
    reFileds = {
    			'msg':fields.String,  需要导入
    			'status':fields.Integer,
    			'eroor':fields.String(default=false) 设定默认	
    		}
    class Cat2Re……
    	def get(self):
    		data ={
    			
    		}
    		return marshal(data=data,fields=r1Fields)
    
    ```
  
  #该方法，不需要使用装饰器，直接利用marshal方法，返回需要两个参数
  
+ **利用 @marshal_with 返回一个对象**

  + 前提有模型->表  如Cat 模型

  ```
  Cat3Apis.py
  
  class Cat3Resource(Resource):
  	r2Fields = {
  		'id' = fields.Integer,
  		'name' = fields.String
  	}
  	
  	r1Fields = {
  		'msg':fields.String(),
  		'status':fields.Integer()
  		#返回对象==> 需要使用嵌套 Nested，其中r2Fields写对象的返回属性
  		'cat':fields.Nested(r2Fields)
  	}
  上面两步做的是格式化输出，模型对象的属性--> 通过Nested方法来获取，如上的r2Fields。
  	@marshal_with(r1..)
  	def get(self):
  		#发起get的请求，根据条件查找，得到对象，返回对象。
		cat = Cat.query.first()
  		data = {
  			'msg':'查询成功',
  			'status':200,
  			'cat':cat,  #--> 这里就不需要在模型中定义to_dict方法。此时cat就是对象--> 但是规定了结构化输出，会返回对象的属性。
  		}
  		return data
  ```
  
  ![1569330231980](C:\Users\msi\AppData\Roaming\Typora\typora-user-images\1569330231980.png)
  
  + 返回页面 出现中文乱码
  
  ```
  //在manager.py文件中添加下面一行代码。
  app  = create_app('develop')
  # 解决中文乱码
  app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
  
  ```
  
  **利用 marshal 返回一个列表**
  
  ```
  返回列表
  Cat4Apis.py
  
  from flask_restful import Resource, marshal, fields
  
  from App.models import Animal
  r2Fields = {
      'id':fields.Integer,
      'name':fields.String,
  }
  r1Fields = {
      'msg': fields.String,
      'status': fields.Integer,
      #注意：需要先利用Nested转换，在使用List转换。
      'animals': fields.List(fields.Nested(r2Fields))
  }
  class Cat4Resource(Resource):
      def get(self):
          animals = Animal.query.all()
          data = {
              'msg':'ok',
              'status':200,
              'animals':animals,
          }
  		return marshal(data=data,fields=r1Fields)==> 需要调用，则是全局变量
  ```

![1569330201498](C:\Users\msi\AppData\Roaming\Typora\typora-user-images\1569330201498.png)

**字典为啥无序**

​		因为底层使用的set集合，而集合set的底层有2个判断，一个是算法不让不允许重复的，还有一个判断是hash==>无序

+ #### 结构化输入-- reqparse 

  + 步骤：

    + ```
      //在apis文件夹下文件中-->需要结构化输入的py文件
      1、parse = reqparse.RequestParser()
      
      add_argument的参数：name --> 接收参数的名字； type --> 类型；required -->请求正确；help--> 当你没穿参数时的提示。
      2、parse.add_argument(name='name',type=str,required=True,help='name为空了')
      
      3、parse = parse.pare_args()  #必须放在方法内
```
      
  + 例子 `api 中 Cat5Apis文件 `
  
  ```
  form ……………… 
  
  parse = request.Requestparse()
  #parse.add_argument(name='name',type=str,required=True,help='name为空了')
  parse.add_argument(name='age',type=int,required=True,help='age必须写')
  
  class Cat5Resource():
  	def get(self):
          p = parse.parse_args()   #必须在请求的方式上面
          name = p.get('name')
          # 如果没有传参数，那么会提示你 上面定义的help内容
          print(name)
          return { 'msg':'ok'}
      def post(self):
      	p = parse.parse_args()   #必须在请求的方式上面
          age = p.get('age')
          # 如果没有传参数，那么会提示你 上面定义的hel内容
          print(age)
          return { 'msg':'ok'}
```
  
  + 注意：add_argument的参数

![1569331738439](C:\Users\msi\AppData\Roaming\Typora\typora-user-images\1569331738439.png)

如果没有传递参数的话，会提示返回help的信息，如果按照正常传的参数，则返回状态status为 200。