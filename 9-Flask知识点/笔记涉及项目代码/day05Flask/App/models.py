from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Parent(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32),unique=True)
    children = db.relationship('Child',backref='parent',lazy=True)

class Child(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32),unique=True)
    parent_id = db.Column(db.Integer,db.ForeignKey('parent.id'))


#建立多对多模型，，注意需要模型迁移，才形成表
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32),unique=True,nullable=True)
    sex = db.Column(db.Enum('男','女'))
    age = db.Column(db.Integer)

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32),nullable=True)

class Collection(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    #注意：多对多关系,是通过另一张表来实现两者的关系，设置外键的方式也有所不同
    u_id = db.Column(db.ForeignKey(User.id))
    m_id = db.Column(db.ForeignKey(Movie.id))

    num = db.Column(db.Integer,default=1) #类似于购物车的功能，如果数据一样，累加，否则默认为1
