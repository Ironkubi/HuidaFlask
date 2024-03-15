from ext import db


class BaseModel(db.Model):
    __abstract__ = True  # 为True抽象类，不能单独作为模型
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
