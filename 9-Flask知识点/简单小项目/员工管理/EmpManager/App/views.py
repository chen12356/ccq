
from flask import Blueprint, render_template, request, redirect, url_for

from App.models import User, db

blue = Blueprint('blue',__name__)


@blue.route('/index/')
def index():
    print('1234')
    return 'index'


@blue.route('/userList/')
def userList():
    users = User.query.all()

    return render_template('userList.html',users=users)

@blue.route('/userAdd/',methods=['get','post'])
def userAdd():
    if request.method == 'GET':
        return render_template('userAdd.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('sex')

        user = User()
        user.name = name
        user.age = age
        user.gender = gender

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('blue.userList'))

@blue.route('/userDelete/')
def userDelete():

    id = request.args.get('id')

    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('blue.userList'))

@blue.route('/userUpdate/',methods=['get','post'])
def userUpdate():
    if request.method == 'GET':
        id = request.args.get('id')
        user = User.query.get(id)

        return render_template('userUpdate.html',user=user)

    if request.method == 'POST':
        id = request.form.get('id')
        user = User.query.get(id)

        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('sex')

        user.name = name
        user.age = age
        user.gender = gender

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('blue.userList'))