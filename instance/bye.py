from flask import Blueprint, request, g
from .decoration import ensure_running
# url_prefix指的是路由的前缀，访问时应该是127.0.0.1/a/bye
# __name__指的是当前这个模块的名字。如果直接运行这个文件的话__name__==__main__
# 通过__name__作为唯一标识来区分各个蓝图
app_bye = Blueprint('bye123', __name__, url_prefix='/a')
@app_bye.route('/bye')
@ensure_running
def bye():
    if request.path.startswith('/a'):
        return '1'
    else:
        return '2'

def test():
    return g.temp
    # return g.temp