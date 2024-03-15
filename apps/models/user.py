from ext import db
from apps.models import BaseModel

class User(BaseModel):
    __tablename__="user"
    name = db.Column(db.String(50))
    address = db.relationship('Address', backref='user',uselist=False)

class Address(BaseModel):
    __tablename__="address"
    street = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))