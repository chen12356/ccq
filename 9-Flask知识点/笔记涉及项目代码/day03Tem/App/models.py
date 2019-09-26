from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Info(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20))
    sex = db.Column(db.String(8))
    age = db.Column(db.Integer)

    __tablename__ = 'emp_info'

