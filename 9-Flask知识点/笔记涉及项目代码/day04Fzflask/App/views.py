from flask import Blueprint, request

from App.models import db, Dept

blue = Blueprint('blue',__name__)

@blue.route('/createTable/')
def create_table():
    db.create_all()
    return '创建成功'

@blue.route('/droptable/')
def droptable():
    db.drop_all()
    return '删除成功'

#给dept模型添加数据 一个对象
@blue.route('/adddept/')
def addDept():
    d = Dept()
    d.name = '李四'
    d.age = 23
    db.session.add(d)
    db.session.commit()
    return '添加成功'
#添加多个对象  注意：add_all([])
@blue.route('/addList/')
def addList():
    d1 = Dept(name='周杰伦',age=23)
    d2 = Dept(name='孙红雷',age=45)
    d3 = Dept(name='王祖贤',age=35)
    d4 = Dept(name='吴京',age=55)
    d5 = Dept(name='王宝强',age=44)
    d6 = Dept(name='张柏芝',age=33)
    d7 = Dept(name='朱茵',age=22)
    db.session.add_all([d1,d2,d3,d4,d5,d6,d7])
    db.session.commit()
    return '多个数据插入成功'
#删除数据，前提是查询，删除哪个数据
@blue.route('/deleteDept/')
def deleteDept():
    d = Dept.query.filter(Dept.id==3).first()#找到id为3的用户，注意用filter主键可以这样写，其他要写全
    print(d.name)
    print(type(d))
    db.session.delete(d)
    db.session.commit()
    return '删除第一条数据（前提是先查询到，）'
#修改数据，前提也要查询，要修改哪个数据
@blue.route('/updateDept/')
def updateDept():
    d = Dept.query.filter(Dept.name=='王宝强').first()  #注意：BaseQuery对象要用all、one、first等方法来等到模型对象
    d.name = '连佳娜'
    db.session.add(d)
    db.session.commit()
    return '修改姓名'

#DQL
#查询单个数据
@blue.route('/getone/')
def getOne():
    d = Dept.query.first() #得到第一个值，注意没有last
    print(d.id,d.name,d.age)

    d2 = Dept.query.get(5) # 获取id为5的对象
    print(d2.id,d2.name,d2.age)

    return '查询单个成功'
#查询结果集，家判断条件
@blue.route('/getResult/')
def getResult():
    #方法all()
    d_list = Dept.query.all()
    print(d_list)
    print(type(d_list))  #是一个list
    for d in d_list:
        print(d.id,d.name,d.age)
    #方法 filter  ==> 注意等号提哦条件为 两个 ==
    d_list1 = Dept.query.filter(Dept.age > 30)

    print(d_list1)
    print(type(d_list1))  #是一个baseQuery对象，需要 遍历得到模型对象
    for d in d_list1:
        print(d.id,d.name,d.age)
    print('=============')
    #方法filter_by  ==> 同样是一个basequery对象，但是 条件 = 一个等号
    d3 = Dept.query.filter_by(id=2).first()
    print(d3.id,d3.name,d3.age)


    #其余方法：
    '''比如:查看字符的开头、结尾，是否包含
    filter(Student.name.startswith('小'))  ==>找 ’小‘ 开头的
	filter(Student.name.endswith('1'))  ==> 结尾的 字符
	filter(Student.name.contains('小'))  ==> 找到 包含 '小' 字的名字
    '''

    return '查询结果集'

#数据筛选
#排序、limit、offset
@blue.route('/testFilter/')
def testFilter():
    d_list = Dept.query.order_by('age')
    print(type(d_list)) #得到的是一个BaseQuery对象
    for d in d_list:
        print(d.id,d.name,d.age)
    print('+++++++++++++++++++++++=+++')
    #倒序
    d_list1 = Dept.query.order_by(db.desc('age'))
    for d in d_list1:
        print(d.id, d.name, d.age)

    print('+++++++++++++limit++++++++=+++')
    d_list2 = Dept.query.limit(4)
    for d in d_list2:
        print(d.id, d.name, d.age)
    print('+++++++++++++offset++++++++=+++')
    d_list3 = Dept.query.offset(4)
    for d in d_list3:
        print(d.id, d.name, d.age)

    print('+++++++++++++一页3条数据，显示第二页数据++++++++=+++')
    d_list4 = Dept.query.limit(3).offset(3)
    for d in d_list4:
        print(d.id, d.name, d.age)

    print('+++++++++++++按照年龄排序，进行分页，显示第二页数据++++++++=+++')
    d_list5 = Dept.query.order_by('age').offset(3).limit(3)
    for d in d_list5:
        print(d.id, d.name, d.age)

    return '数据的筛选'

#分页器pagina
#1、原生代码
@blue.route('/pagina/')
def pagina():
    page = request.args.get('page')
    page_per = request.args.get('page_per')
    d_list = Dept.query.limit(int(page_per)).offset(int((page-1)*int(page_per)))
    for d in d_list:
        print(d.id, d.name, d.age)
    return '原生分页'