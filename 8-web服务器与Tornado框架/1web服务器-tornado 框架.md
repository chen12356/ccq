### 一、web 服务器

​	web  指的 是**万维网**， 这样数据就不会只在本地访问，其他用户可以访问。

+ http 协议 ==> 超级文本传输协议
+ html   ==> 超级文本标记语言
  + **什么是超文本**：指的是包含各种各类的东西，比如除了一些文本，还有一些样式表，视频、音乐等，多种类型文件。
+ http协议，底层是**基于TCP协议**  （注意：只是依赖tcp的可靠性）
  + **构建在长连接基础上的短连接协议**。
  + tcp协议：
    + 建立连接：三次握手
    + 断开连接：四次握手
    + 可靠：**依靠内部对数据的校验工作**，保证数据的可靠性。防止数据的缺失等
    + 长连接协议：（可以想象成打电话，两者是持续不断的连接，如如水流一样 ），**而http自己却是短连接。**
      + 浏览网页并不用和服务器一直保留连接，所以http只是利用了tcp的可靠性
+ **html的服务器server** ，本质的话就是**socket**连接、前端和后端的规定数据的格式--http等协议的报文

```
#!/usr/bin/env python    ==>env可以帮我们找到合适的python
import socket
sock = socket.socket(socket.AF_INT,socket.SOCK_STREAM)
sock.setsockopt(socket.SQL_SOCKET,socket.SO_REUSEADDR,1) #为sock打开地址的重新选项，这样就可以一直用了该地址端口了
addr = sock.bind(('127.0.0.1',8000))  #1024端口是系统占用的
sock.listen(100)
print("服务器已运行，等待连接") 
#在这可以直接定义一个死循环，来一直等待客户端的连接。

cli_sock,cli_addr = sock.accept() #等待连接，两个返回值

cli_data=cli_sock.recv(1024) #接收客户端传来的数据，1024是接收缓冲区的大小,(如果浏览器访问那么是浏览器给服务器发送的请求报文)
# 定义响应报文
html=b'''
HTTP/1.1 200 OK

<html>
	<head>	
		<title>home</home>
	</head>
	<body>
		hello word
	</body>
	
</html>
'''

cli_sock.sendall(html)  #sendall发送了全部数据，b指bytes数据。不使用的话需要编码encode
cli_sock.close()  #断开连接


```

**注意：**浏览器对服务端的进行访问，那么需要给浏览器返回的数据是html格式才可以，这样浏览接收到服务端的数据，才可以在浏览器上显示。

response headers  ==> 响应报文，第一行指的是响应的状态

request headers  ==>请求的报文

+ 区分url，对发来的数据分析 （下面的例子是不使用框架）

  + 服务端会接收客户端发送的请求报文

    + 如：GET  /foo/bar  HTTP/1.1   ==>响应报文的第一行
    + /foo/bar 是客户端的那个url地址。那么需要获取该地址，

  + ```
    def get_url(request_str):
    	'''从请求报文中获取请求的 URL'''
    	url = request_str.split('\n')[0].split('')[1]   
    	return url
    ```

  + ```
    #!/usr/bin/env python    ==>env可以帮我们找到合适的python
    import socket
    sock = socket.socket(socket.AF_INT,socket.SOCK_STREAM)
    sock.setsockopt(socket.SQL_SOCKET,socket.SO_REUSEADDR,1) #为sock打开地址的重新选项，这样就可以一直用了该地址端口了
    addr = sock.bind(('127.0.0.1',8000))  #1024端口是系统占用的
    sock.listen(100)
    print("服务器已运行，等待连接") 
    # 定义响应报文,注意下面的响应头需要和下面的html的文本需要加一个空行，否则整个都被当做的了响应头
    html='''
    HTTP/1.1 200 OK
    
    <html>
    	<head>	
    		<title>home</home>
    	</head>
    	<body>%s</body>  
    </html>
    '''
    //从请求报文中获取url地址
    def get_url(request_str):
    	'''从请求报文中获取请求的 URL'''
    	url = request_str.strip().split('\n')[0].split('')[1]   
    	return url
    #定义循环
    while True:
    	cli_sock,cli_addr = sock.accept() #等待连接，两个返回值
    	cli_request=cli_sock.recv(1024).decode("utf8") #(如果浏览器访问那么是浏览器给服务器发送的请求报文)
    	url = get_url(cli_request)  #获取url地址
    	#根据url来判断，返回的响应报文
    	if url=='/foo':
    		response = html % '爱妃退下'
        elif url=='/bar':
        	response = html % 'lalala'
        else:
        	response = html % 'hello word'
    	# 根据不同的url返回不同的html
    	cli_sock.sendall(response.encode('utf8'))
    	cli_sock.close()  #断开连接
    ```
```
    
+ 格式化输出方式
  
  + %s
  
      + ````
        '----%s----' % 'nihao '
````

  + format
  
      + ```
        '----{}---{}'.format('abc','x')
        ```
  ```
      
    + ```
      直接用 f
      abc = 123
      x = 456
      f'===={abc}==={x}=='   ===>这样也是可以的。
  ```


### 二、web框架

把开发一个网站需要各种各样的东西全部整合到一起，这指的就是 **web框架思维**

当你用户访问服务器，查找数据库，将数据融合到模版中(该模版指的就是网页模版)，返回到用户端，展示个用户看  ===>  动态的网页 ==>ajax、vue等技术， 我们学的后端动态页面技术，并且和这些技术结合使用

#### 1、web服务器原理

用户传入数据访问前端，将**数据作为参数传递给后端**，后端python程序对该数据进行逻辑运算操作、及数据库的操作，然后处理完数据，直接给前端，这就是前后端分离   

#### 常见的web框架

+ **Django**
  + 最早期为美国的杂志报刊能够大量、快速的开发。全能型框架，大而全，插件丰富，文档丰富，社区活跃（指一个交流团体，讨论的比较活跃）、内部耦合比较紧（耦合：比如一个模块有很多的函数，如果你删除了某个函数，那么迁一发动全身）
+ **Flask**
  + 框架本身包含的东西很少，比如没有数据库处理，微型框架，所以围绕的插件非常多，极其灵活，极低耦合
+ **Tornado**
  + 性能最好（除了Sanic）,因为底层使用异步处理(比如你在执行一个功能，那么还可以单开另一个处理)，用的是协程，事件驱动(epoll)多路复用，速度快。
  + ioloop 该模块使驱动了 Tornado框架的核心。
  + web 模块
+ Bottle
  + 简单，单文件框架，3000多行，适合初学者学习（了解web的底层）
+ **web.py**
  + 是一个美国的黑客写的，也参与过markdown的开发，15岁就参与这个markdown开发，相当的厉害，天才，现已经去世了
+ falcon
  + 适合写api接口
+ Quixote
  + 出现相当早，豆瓣使用依然就是该框架，豆瓣不换是因为成本太大，底层涉及的全都要换。
+ **Sanic**
  + 底层使用了uvloop，底层一些C语言的异步处理。uvloop的底层还是封装了epoll。所有性能相当好，不是很稳定

#### 2、Tornado 入门(龙卷风,读音：特内斗)

现在是由 facebook的在维护(被facebook收购了，保留了tornado框架)

**查看源代码**：`pip download  tornado`  ==>下载，解压，进入指定tornado目录，里面的文件都是源代码。适合开源的应用。用法一样

`tornado.web.RequestHandler`   ==>继承该模块，用于页面请求的处理器

def get(self)  ==>定义处理get请求方法。同样也可以定义 post、head等出来的方法，定义同名的请求方法即可。

```
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):   ==>定义该类，继承了该模块，用于指定连接的请求的处理器。里面定义的方法也是，和请求方式同名的方法。
	def get(self):
		self.write("hello word")  #write直接写入了html中，这里底层把一些HTML的一些信息设置好了
def make_app():
	# 这里调用了tornado.web中的Application
	return tornado.web.Application([
		(r"/",MainHandler),  # 这个斜杆指的是路径，路由，默认访问到根路径，r'/'可以正则匹配。比如（r'/book/.+'）==> 以book开头的，.+ 是匹配任何，
	])
		
	
if __name__ == "__main__":
	app = make_app()   ==>运行整个框架的整体，目的就是让app运行起来
	app.listen(8888)   ==>参数1：端口号，参数2：ip地址，默认不写，是指定当前ip地址
	loop = tornado.ioloop.IOLoop.current()  ==>，current指的是游标，当前的位置。得到的是个loop对象，用来驱动协程的。
	loop.start()
```

#### 3、启动参数

在linux的命令行中运行，可以和脚本使用一样，后面添加参数

比如` ./xxxx.py --help   `   该--help便是里面的参数

需要导入模块：`from tornado.options import parse_command_line,define,options`

其中使用**define**来定义参数，如下例子

```
格式：define('参数名',default='默认值',help='参数介绍',type=参数类型比如int、str等)

define('xyz',default='abcd',help='测试参数',type=str)
define('host',defaule='0.0.0.0',help='主机地址',type=str)

if __name__="__main__":
	parse_command_line()
	print(options.xyz)
```

+ 不指定参数返回的默认参数。

![1568037724904](./img/1568037724904.png)

![1568037815151](./img/1568037815151.png)

常见的局域网地址：

10.x.x.x   ==>该局域网内的都可以访问了    

172.16.x.x

192.168.x.x

```
//选项模块  tornado.option   命令行参数 parse_command_line,difine,options

import tornado.ioloop
import tornado.web
from tornado.options import parse_command_line,difine,options
define('host',defaule='0.0.0.0',help='主机地址',type=str) #0.0.0.0指的是绑定当前机器上所有的ip地址，数据库不能这么用，如果绑定了0.0.0.0，并且在外网上，那么全世界人都能访问你的数据库了。localhost等效于127.0.0.1 ，localhost本机内的域名，
define('post',defaule='8888',help='主机端口',type=int)


class MainHandler(tornado.web.RequestHandler): 
	def get(self):
		self.write("hello word")  
def make_app():
	# 这里调用了tornado.web中的Application
	return tornado.web.Application([
		(r"/",MainHandler),  # 这个斜杆指的是路径，路由，默认访问到根路径
	])
		
	
if __name__ == "__main__":
	app = make_app()   ==>运行整个框架的整体，目的就是让app运行起来
	app.listen(options.post,options.host)   ==>用options传递参数
	loop = tornado.ioloop.IOLoop.current() 
	loop.start()
```

#### 4、路由处理

```
把url转换到tornado里面，如何操作


class Foo(tornado.web.RequestHandler): 
	def get(self):
		self.write("无法无天")  
class Bar(tornado.web.RequestHandler): 
	def get(self):
		self.write("无懈可击")  
def make_app(): //用户请求，先去下面的url对比，如果一样，那么执行对应的视图类
	return tornado.web.Application([
		(r"/",MainHandler), 
		(r"/foo",Foo),   =>需要重写该处理方法
		(r"/bar",Bar),   ==>前者是url，后者是指定处理的数据的类
	])
```

#### 完整的url

**一个完整的url**(唯一资源的定位)  `http://xxxxx.com:80/foo/bar/xx.html?aaa=123&bb=456#top`

​	更早期的时候，开头有用户名和密码 比如： `http://root:passwd@xxxx.com……`

+ 第一层是协议，比如下面的
  + http://
  + https
  + ftp
  + socks
  + redis
  + mysql
+ 第二层是主机名：比如 xxxxx.com:80
+ 第三层是绝对路径：比如: /foo/bar/xx.html   如果只有一个 / 当前的服务器的根路径
+ 第四层是参数对应的数据  比如：?aaa=123&bb=456  从? 开始，后面就是参数对应的数据
+ 第五层  #top 指的是 锚点，

#### 5、处理get和post请求

比如：127.0.0.1:8000/?name=abc    ==>把这个参数name的值打印在网页上

```
//处理get请求
class MainHandler(tornado.web.RequestHandler): 
	def get(self):
		name = self.get_argument('name')  ==>定了一个参数name，通过get_argument取值。
		self.write("hello,%s"%(name))  ==>此时格式化输出该参数对应的值
//通过对对应函数参数的设定，那么你在url中对应传的参数，会获取到。

//处理post请求，需要用到get请求，以及表单。
class Bar(tornado.web.RequestHandler): 
	def get(self):
		html = (
			'<form action="/test/post">'   #注意：action是url地址
			'姓名:<input type="text" name="name">'
			'<br>'
			'城市:<inpue type="text" name="city">'
			'<br>'
			'<input type="submit">'  #第一次访问是get，提交后，为post请求了,此时执行post函数
			'<form>'
		)
		self.write(html)  
	def post(self):    //需要使用get，表单来传输
		name = self.get_argument('name')
		city = sele.get_argument('city')
		self.write('%s 生活在 %s' %(name,city))
```

**http请求的方法**

post  修改、创建数据

get  从服务器获取信息，查看信息，

put 对post进行细化，把post中修改服务器信息，建议用put

delete  删除

head  用来服务器获取东西，但是只获取一个请求头，不会获取具体信息，一般用作网页的测试，一些状态码。

patch  对post更细化版本，对数据一些更新

options  查看服务器支持的请求方法。，



练习：

把表的字段建立成类的属性，一对一，数学上叫映射  ORM   下篇笔记详细。

1.数据用户传入id显示对应信息

2.根据用户传入的数值修改用户修改