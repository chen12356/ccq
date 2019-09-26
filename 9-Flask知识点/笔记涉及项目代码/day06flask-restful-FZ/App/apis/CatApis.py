from flask_restful import Resource


class CatResource(Resource):
    #定义不同请求的方式的函数，返回对于的数据
    def get(self):
        data = {
            'msg':'ok',
            'status':200,
        }
        return data

    def post(self):
        data = {
            'msg': 'ok',
            'status': 200,
        }
        return data

    def put(self):
        data = {
            'msg': 'ok',
            'status': 200,
        }
        return data

    def patch(self):
        data = {
            'msg': 'ok',
            'status': 200,
        }
        return data

    def delete(self):
        data = {
            'msg': 'ok',
            'status': 200,
        }
        return data
