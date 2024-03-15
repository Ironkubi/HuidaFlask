from flask_sqlalchemy import SQLAlchemy

# 创建组件对象
db = SQLAlchemy()

class User(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.relationship('Address', backref='user',uselist=False)

class Address(db.Model):
    __tablename__="address"
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))