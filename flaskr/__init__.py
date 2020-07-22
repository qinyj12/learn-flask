import os
from flask import Flask, redirect, url_for

def create_app(test_config=None):
    # instance_relative_config=True指的是配置文件是相对于instance_folder的相对路径
    # 也就是在本文件·父·目录下的的instance目录，和本文件不属于同一目录。
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        # 用于一些需要秘钥的场景
        SECRET_KEY='dev',
        # 数据库文件
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # 如果test_config=None，意即没有独立的配置文件。
    if test_config is None:
        # 再次尝试加载instance_path里的配置文件，如果silent是True，则即使不存在也不会报错
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 如果test_config != None，意即有独立的配置文件。
        # 只要在生产环境中改掉test_config一个值就好了，不用再一处一处修改
        app.config.from_mapping(test_config)

    # 创建instance_path目录，因为要保证这个目录存在
    try:
        os.makedirs(app.instance_path)
    # 如果instance_path已存在，就会报错，所以用except忽略
    except OSError:
        pass
    
    from . import bye, date, hello
    app.register_blueprint(bye.app_bye)
    app.register_blueprint(date.app_date)
    app.register_blueprint(hello.app_hello)

    return app