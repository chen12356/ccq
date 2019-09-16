局域网（内网）：10.x.x.x /172.16.x.x /192.168.x.x

### linux下软件的安装

+ sudo命名 ：以**管理员的身份执行**。
+ Ubuntu中的**apt命令**：
  - search：搜索 ·`apt search xxx`
  - show：查看详情
  - install：安装包
  - remove：删除
  - update：更新软件园
  - upgrade：升级软件 
  - autoremove：自动删除无效的安装包

连接远程服务器

+ 命令：ssh  root@服务器ip地址
+ 输入服务器密码
+ 登录服务器成功，[root@服务器用户名 ~]#
+ ctrl+end 退出

云服务中的yum命令：

**yum install** python3  ==>给服务器安装了python3

卸载 yum remove  



ls 得到当前目录的文件， 

ls -l 以列表的形式返回。

sudo （super  do）以超级用户身份执行

一键安装软件

man手册、gcc make 编译，openssl 是一个加密的库（平时用的加密协议都在里面），tree树，vim终端一个编辑器、curl发送请求，浏览器等得到网页源代码、telnet 用来检查网络状态、traceroute 追踪网络路由器路径(比如traceroute baidu.com，那会它会返回当前开始到访问百度的整个路径)、wget 从网络下载东西、libbz2 软件的源代码、git做代码管理的工具、

安装python

`sudo apt install python3.6`

安装pycharm

`https//www.jetbrains`

```
先找到该文件
利用tar 解压文件
tar -xzf  其中-x是解压以gz的压缩包，
ls 此时可以看出是否多了该目录
cd 该软件目录里面
cd 该目录下的bin目录下
ls
运行./pycharm.sh 这样就可以执行该软件了

```

安装vnc

```

```

软件包

```
1、centOS 软件包是 rpm
2、Ubuntu  软件包是 deb
这linux下直接双击，点击安装即可
```



