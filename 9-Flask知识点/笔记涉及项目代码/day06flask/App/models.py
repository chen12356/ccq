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

