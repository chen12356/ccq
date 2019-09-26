from flask_restful import Resource, fields, marshal_with

from App.models import Animal


class Cat3Resource(Resource):
    #利用 @marshal_with 返回一个对象
    #使用方法--> fields.Nested --> 嵌套，里面的值也是返回的属性
    r2Fiedls = {
        'id':fields.Integer,
        'name':fields.String,
    }

    r1Fields = {
        'msg':fields.String,
        'status':fields.Integer,
        'animal':fields.Nested(r2Fiedls)
    }
    @marshal_with(r1Fields)
    def get(self):
        animal = Animal.query.first()
        data = {
            'msg':'查询成功',
            'status':200,
            'animal':animal
        }
        return data

