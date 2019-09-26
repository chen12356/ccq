from flask_restful import Resource, fields, marshal_with


class Cat1Resource(Resource):
    #定义结构化输出
    r1Fields = {
        'msg':fields.String,
        'status':fields.Integer,
        'eroor':fields.String(default='false'),
    }

    #需要一个装饰器 mershal_with(r1Fields)  需导入
    @marshal_with(r1Fields)
    def get(self):
        data = {
            'msg':'ok',
            'status':200,
        }
        return data
#1、结构化数据多，返回的数据少 ===> 那么多于的结构化数据返回默认值
#    （Integer类型  默认 0, String类型默认为 null，也可以自己定义default默认值）
#2、结构化少，返回的数据多，==>按照结构化的返回，多的自动过滤
#3、两种一样，那么就正常输出

#marshal 还有另一种用法 ==> 不使用装饰器的写法
'''不适用装饰器写法
    以上代码做例子，将  @marshal_with(r1Fields)  去除
    在方法的返回值使用marshal
    #注意：此时r1Fields => 是全局变量
    return marshal(data=data,fields=r1Fields)
'''