from flask import Flask
from model import *

app = Flask(__name__)
# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tester:123456@10.1.1.167:3306/huidaflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# 初始化数据库
with app.app_context():
    db.init_app(app)
    db.drop_all()
    db.create_all()
    
#测试    
@app.route('/')
def hello_world():  # put application's code here
    u1 = User(name="yiyi")
    add1 = Address(street="street1")
    u1.address = add1
    db.session.add_all([u1])
    db.session.commit()
    add2 = Address(street="street2")
    #u1.address.append(ad1) #会报错
    db.session.commit()
    u1name =  add1.user.name
    print("-------------")
    print(u1name) #yiyi
    counts = u1.address
    print(counts.street) #street1
    #换一个地址
    u1.address = add2
    counts = u1.address
    db.session.commit()
    print(counts.street) #street2
    return "成功"

# 运行代码
if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0', port=81, debug=True))
