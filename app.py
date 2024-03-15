from flask import Flask
from ext import db
import config

app = Flask(__name__)
# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tester:123456@10.1.1.167:3306/huidaflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)      #载入config.py中的配置信息
 
    db.init_app(app)  # app绑定数据库db
 
    return app

    
@app.route('/')  
def hello_world():  
	return 'Hello World!'  


# 运行代码
if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0', port=81, debug=True))
