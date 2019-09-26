from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Info(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(32))
    name = db.Column(db.String(32))
    password = db.Column(db.String(32))
    sex = db.Column(db.String(8))
    age = db.Column(db.Integer,default=0)
    phone = db.Column(db.Integer)
    ask = db.Column(db.String(256))
    __tablename__ = 'emp_info'
