from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Animal(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32),unique=True)
    #因为json不能返回对象，在此处定义方法，将这段以字典的形式返回
    def to_dict(self):
        return {'id':self.id,'name':self.name}

