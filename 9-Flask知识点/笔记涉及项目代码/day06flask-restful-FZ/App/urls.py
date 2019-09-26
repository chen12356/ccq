from flask_restful import Api

from App.apis.Cat1Apis import Cat1Resource
from App.apis.Cat3Apis import Cat3Resource
from App.apis.Cat4Apis import Cat4Resource
from App.apis.Cat5Apis import Cat5Resource
from App.apis.CatApis import CatResource

api = Api() #创建api对象

def init_urls(app):
    #初始化api
    api.init_app(app=app)

api.add_resource(CatResource,'/cat/')
api.add_resource(Cat1Resource,'/cat1/')
api.add_resource(Cat3Resource,'/cat3/')
api.add_resource(Cat4Resource,'/cat4/')
api.add_resource(Cat5Resource,'/cat5/')
