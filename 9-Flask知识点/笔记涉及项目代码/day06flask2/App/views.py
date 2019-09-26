from flask import Blueprint, request, current_app, render_template, jsonify

from App.ext import cache
from App.models import Animal, db

blue = Blueprint('blue',__name__)

@blue.route('/test/')
def test():
    return 'xxxx'

#===================================
#前后端分离---添加数据
#注意：前后端分类没有表单的
@blue.route('/toRegister/')
def toRegister():
    return render_template('register.html')
@blue.route('/Register/')
def register():
    name = request.args.get('name')
    print(name)
    animal = Animal()
    animal.name = name
    db.session.add(animal)
    db.session.commit()

    data = {
        'msg':'ok',
        'status': 200,
        'animal':animal.to_dict()
    }
    print(data.get('animal'))
    return jsonify(data)
@blue.route('/index/')
def index():
    return '交互完成'

#======================================
#前后端分离 --- 查询
#注意：前后端分离是不可以直接传输对象的。所以在模型类中定义一
# 个方法获取数据。如定义to_dict方法
@blue.route('/getAnimal/')
def getAnimal():
    #animal = Animal.query.frist() ==> 查询单个对象
    animal_list = Animal.query.all()  #查询多个对象
    animals = []
    for animal in animal_list:
        animals.append(animal.to_dict())
    #print(animals)
    data = {
        'msg':'ok',
        'status':200,
        'animals':animals
    }
    return jsonify(data)

@blue.route('/toGetAnimal/')
def toGetAnimal():
    return render_template('getAnimal.html')

#=========================================
#修改
@blue.route('/testPut/', methods=['put', 'patch'])
def testPut():
    animal = Animal.query.first()
    animal.name = 'python'
    db.session.add(animal)
    db.session.commit()
    data = {
        'msg': 'ok',
        'status': 200,
        'animal': animal.to_dict()
    }
    return jsonify(data)

#========================================
#删除 delete 请求
@blue.route('/testdelete/',methods=['DELETE'])
def testdelete():
    animal = Animal.query.first()

    db.session.delete(animal)
    db.session.commit()
    data = {
        'msg':'ok',
        'status':200,
        'animal':animal.to_dict()
    }
    return jsonify(data)