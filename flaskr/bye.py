from flask import Blueprint
# url_prefix指的是路由的前缀，访问时应该是127.0.0.1/a/bye
# __name__指的是当前这个模块的名字。如果直接运行这个文件的话__name__==__main__
# 通过__name__作为唯一标识来区分各个蓝图
app_bye = Blueprint('bye123', __name__, url_prefix='/a')
@app_bye.route('/bye')
def index():
    return __name__