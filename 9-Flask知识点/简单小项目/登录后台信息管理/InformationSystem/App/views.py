from flask import Blueprint, request, url_for, render_template
from werkzeug.utils import redirect

from App.models import Info, db

blue = Blueprint('blue',__name__)

@blue.route('/base/')
def base():
    pass
    return render_template('base.html')
@blue.route('/login/',methods=['GET','POST'])
def login():
    return render_template('Login.html')

@blue.route('/checkLogin/',methods=['GET','POST'])
def checkLogin():
    username = request.form.get('username')
    password = request.form.get('pwd')
    usernames = Info.query.filter(Info.username==username).filter(Info.password==password)
    if usernames.count() > 0 :
        print('在数据库中')
        return redirect(url_for('blue.userList'))
    else:
        return redirect(url_for('blue.login'))

@blue.route('/register/')
def register():
    return  render_template('register.html')

#添加数据
@blue.route('/addInfo/',methods=['GET','POST'])
def add_info():
    emp = Info()
    emp.username = request.form.get('username')
    emp.name = request.form.get('name')
    emp.password = request.form.get('pwd')
    emp.age = int(request.form.get('age'))
    emp.phone = int(request.form.get('phone'))
    emp.ask = request.form.get('ask')
    sex = request.form.get('sex')
    if sex=='m':
        emp.sex = '男'
    else :
        emp.sex = '女'
    db.session.add(emp)
    db.session.commit()

    return redirect(url_for('blue.login'))

@blue.route('/userList/',methods=['GET','POST'])
def userList():
    page = int(request.args.get('page',1))
    per_page = int(request.args.get('per_page',5))
    info_list = Info.query.paginate(page=page,per_page=per_page)
    return render_template('userList.html',info_list= info_list)

@blue.route('/userInfo/')
def userInfo():
    id = request.args.get('id')
    user = Info.query.get(id)
    print(user.id)
    return render_template('userInfo.html',user=user)

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
