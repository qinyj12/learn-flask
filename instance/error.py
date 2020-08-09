from flask import render_template, Blueprint, abort, jsonify
from .decoration import ensure_running

@ensure_running
def page_not_found(error):
    # 因为是从factories.__init__调取的，所以模板也是在factories/templates/里
    return render_template('404.html'), 404

def internal_server_error(e):
    # 可以自定义一个error页面
    # <h1>依然是异常码对应的含义（500 => Internal Server Error）
    # 下面的<p>则是自定义的e
    return jsonify(error = str(e)), 500

app = Blueprint('error_test', __name__, url_prefix = '/error')

# 这是用来测试error的
@app.route('/404')
def index():
    abort(404)

@app.route('/500')
def index2():
    # description的值就是自定义的异常
    abort(500, description = '自定义错误：500')

# 再定义一个不使用description的视图
@app.route('/5002')
def index3():
    abort(500)
