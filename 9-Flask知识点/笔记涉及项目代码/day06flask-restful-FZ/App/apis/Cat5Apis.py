
from flask_restful import reqparse, Resource

parse = reqparse.RequestParser()
parse.add_argument(name='name',type=str,required=True,help='name为空了')
parse.add_argument(name='age',type=str,required=True,help='age为空了')

class Cat5Resource(Resource):

    def get(self):
        p = parse.parse_args()
        name = p.get('name')
        print(name)
        return {'msg':'ok'}

    def post(self):
        p = parse.parse_args()  # 必须在请求的方式上面
        age = p.get('age')
        # 如果没有传参数，那么会提示你 上面定义的hel内容
        print(age)
        return {'msg': 'ok'}