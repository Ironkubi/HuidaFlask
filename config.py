
#数据库配置信息
HOSTNAME = '10.1.1.167'
PORT     = '3306'
DATABASE = 'huidaflask'
USERNAME = 'tester'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
 
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True