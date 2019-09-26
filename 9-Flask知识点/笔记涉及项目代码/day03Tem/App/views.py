from flask import Blueprint, render_template, request, redirect, url_for

from App import db
from App.models import Info

blue = Blueprint('blue',__name__)

@blue.route('/test/')
def test():
    return 'xxxx'

#向页面传递参数
@blue.route('/index/')
def index():
    name = '张三'
    return render_template('index.html',name=name,age=12) #多传的参数不影响页面

#继承 基模板 base.html
@blue.route('/tem2/')
def tem2():
    return render_template('base_a.html')

#继承base_a.html模板, (也就是没有继承基模板)
#问题：子模板中和父模板的变量同名，会覆盖父模板---使用super()方法-- {{ super() }}
@blue.route('/tem3/')
def tem3():
    return render_template('base_b.html')

#导入其他模板 利用 { inclued '名称.html' }
@blue.route('/tem4/')
def tem4():
    return render_template('base_c.html')

#宏定义 macro  (html中用三个方法)
@blue.route('/macro/')
def macro():
    return render_template('macro.html')

#循环语句 for -if
@blue.route('/for_if/')
def for_if():
    socre_list = [56,78,56,34,67]
    return render_template('for_if.html',scores=socre_list)

#过滤器，向叶面传递数据，页面对数据过滤(针对：大小写、空格、反转、处理标签)
@blue.route('/filter/')
def filter():
    code1 = 'abcdefgHI'
    code2 = '   ab cd   '
    code3 = '<h1>我被safe处理了，标签有用了</h1>'
    return render_template('filter.html',code1=code1,code2=code2,code3=code3)

#创建表
@blue.route('/createTable/')
def create_table():
    db.create_all()
    return '创建成功'
#删除表
@blue.route('/dropTable/')
def drop_table():
    db.drop_all()
    return '删除成功'

#添加数据
@blue.route('/addInfo/')
def add_info():
    emp = Info()
    emp.name = '李丽珍'
    emp.sex = '女'
    emp.age =39

    db.session.add(emp)
    db.session.commit()

    return '提交成功'

#通过模型擦查询所有数据  --> 模型(也就是类).query.all()
@blue.route('/findall/')
def findall():
    emp_list = Info.query.all()
    return render_template('emp_info.html',emps=emp_list)

@blue.route('/emp/')
def emp():
    return render_template('emp_info1.html')

@blue.route('/userList/')
def userList():
    page = int(request.args.get('page',1))
    per_page = int(request.args.get('per_page',5))
    info_list = Info.query.paginate(page=page,per_page=per_page)

    return render_template('userList.html',info_list= info_list)

@blue.route('/deleteData/')
def deleteData():
    id = request.args.get('id')
    user = Info.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return  redirect(url_for('blue.userList'))

@blue.route('/updateData/')
def updateData():
    id = request.args.get('id')
    print(id)
    user = Info.query.get(id)
    return  render_template('updateData.html',emp=user)

#实现修改数据
@blue.route('/updateData1/',methods=['GET','POST'])
def updateData1():
    id = request.args.get('id')
    name = request.form.get('name')
    sex = request.form.get('sex')
    age = request.form.get('age')
    save = request.form.get('1')
    ret = request.form.get('0')
    print(age,save,ret)
    if save == '保存':
        if (len(name) == 0 or len(sex) == 0 or len(age) == 0):
            return '含有输入项为空，修改失败'
        user = Info.query.get(id)
        user.name = name
        user.sex = sex
        user.age = age
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('blue.userList'))
    elif ret == '返回':
        return redirect(url_for('blue.userList'))


