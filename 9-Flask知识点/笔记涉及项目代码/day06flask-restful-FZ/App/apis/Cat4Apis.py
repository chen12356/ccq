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
        return marshal(data=data,fields=r1Fields)