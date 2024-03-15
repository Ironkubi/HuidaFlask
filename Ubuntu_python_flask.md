# python

## 安装 virtualenvwrapper

* 安装

  > pip install virtualenv  
    pip install virtualenvwrapper

* 创建目录用来存放虚拟环境

  > mkdir ~/.virtualenvs

* 配置环境变量,修改~/.bashrc文件，添加以下内容

  > vim ~/.bashrc  
    export WORKON_HOME=~/.virtualenvs  
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3  
    export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv  
    source /usr/local/python386/bin/virtualenvwrapper.sh  
  > source ~/.bashrc  

* 常用命令

  > mkvirtualenv -p python3.8 env_name   # 创建虚拟环境  
    cdvirtualenv    # 导航到当前激活环境的目录中  
    cdsitepackages    # 导航到当前激活环境的site-packages目录中  
    workon            # 查看所有的虚拟环境  
    workon env_name       # 切换到xx虚拟环境  
    deactivate      # 退出虚拟环境  
    rmvirtualenv env_name  # 需先退出,再删除  

* 虚拟环境内利用requirements.txt安装

  > pip freeze > requirements.txt   # 进入虚拟环境

## 安装 Flask

* 安装

  > pip install flask  

* 案例

  > 例子  
    from flask import Flask  
    app = Flask(__name__)
    @app.route('/')  
    def hello_world():  
    　　return 'Hello World!'  
    if __name__ == '__main__':  
    　　app.run(app.run(host='0.0.0.0', port=81, debug=True))  
    debug模式。默认是没有开启的  
    修改host。默认情况下是localhost,如果想让在同一个网络下的其他设备可以访问的话，需要修改为0.0.0.0  
    修改port。默认5000  

## 安装 Flask-SQLAlchemy

* 安装

  > pip install flask-sqlalchemy

## 安装 Flask-Migrate

* 安装

  > pip install flask-migrate

* 迁移命令

  > python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade

## 安装 PyMySQL

* 安装

  > pip install pymysql
  