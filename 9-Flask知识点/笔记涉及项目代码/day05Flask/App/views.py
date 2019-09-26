from flask import Blueprint, request

from App.models import Parent, Child, db,User,Movie,Collection

blue = Blueprint('blue',__name__)

@blue.route('/test/')
def test():
    return 'xxxx'

#添加数据，利用父表给子表添加数据
@blue.route('/addParent/')
def addParent():
    p = Parent()
    p.name='父亲'
    c1 = Child()
    c1.name = '儿子1'
    c2 = Child()
    c2.name = ''
    c3 = Child()
    c3.name = '儿子2'
    c4 = Child()
    c4.name = '儿子3'
    #把子表的对象存入列表中，利用父表中定义的children属性，来关联子表
    p.children = [c1,c2,c3,c4]  #利用了children属性，利用方法relationship

    db.session.add(p)
    db.session.commit()
    return '添加成功'

#查询数据，通过父表查询从表 ==> 主查从，正向引用relationship方法
@blue.route('/getChild/')
def getChild():
    #查询父表id为1的 子表关联数据，
    p = Parent.query.get(1)
    childs = p.children  #父表中relationship放=方法定义的属性来查询子表
    for child in childs:
        print(child.name)
    return '通过父表查询从表数据成功'

#从 子表 查询 父表的数据 （反向应用backref）
#找到一个子表对象，利用父表中的relationship方法中backref的反向引用
@blue.route('/getParent/')
def getParent():
    child = Child.query.filter(Child.id==2)[0]
    print(child.parent.name)  #利用反向引用的父表来实现，
    return '从子表中查询父表的数据'

#======================================

#多对多
#1、分别给用户表和电影表添加一些数据
@blue.route('/addUser/')
def addUser():
    users = [
        User(name='张柏芝',sex='女',age=42),
        User(name='周星驰',sex='男',age=53),
        User(name='李四',sex='男',age=33),
        User(name='爱丽丝',sex='女',age=36),
        User(name='朱茵',sex='女',age=18),
        User(name='王宝强',sex='男',age=42)
    ]
    db.session.add_all(users)
    db.session.commit()
    return '多个数据添加成功'
@blue.route('/addMovie/')
def addMovie():
    movies = [
        Movie(name='无间道'),
        Movie(name='功夫'),
        Movie(name='你看起来很好吃'),
        Movie(name='恶灵骑士'),
        Movie(name='极品宝鉴'),
        Movie(name='玉女心经')
    ]
    db.session.add_all(movies)
    db.session.commit()
    return '多个电影添加成功'
#2、现在关联两个张表，同用户传递的参数 用户id和电影id，给该关联表插入数据
#如果插入的数据相同，那么，在订单表中加1，是不是和购物车一样
@blue.route('/addCollection/')
def addCollection():
    u_id = request.args.get('u_id')
    m_id = request.args.get('m_id')
    collections = Collection.query.filter(Collection.u_id==u_id).filter(Collection.m_id==m_id)
    if collections.count() > 0:
        collection = collections[0]
        collection.num = collection.num + 1 #将数量加一
    else:
        collection = Collection()
        collection.u_id = u_id
        collection.m_id = m_id

    db.session.add(collection)
    db.session.commit()

    return '订单表插入成功'

