from flask import Blueprint, g, url_for, redirect, request

app = Blueprint('user', __name__, url_prefix='/user/<user_name>')

# url_value_preprocessor所装饰的函数，会在视图函数被调用之前执行、url路径被预处理时执行
# 他所传入的第二个参数保存了当前请求url上参数的值，仅限在<>内的动态参数，比如本蓝图中的<user_name>
#如果请求的url是'/user/qinyujie/'，那本函数的第二个参数（view_args）就是{'user_name': 'qinyujie'}
@app.url_value_preprocessor
def get_user_name_from_url(endpoint, view_args):
    g.user_name = view_args.pop('user_name')

@app.url_defaults
def add_user_name(endpoint, values):
    values.setdefault('user_name', g.user_name)

@app.route('/')
def index():
    return 'hello %s' % g.user_name

@app.route('/date')
def date():
    return url_for('dateNow.index', dater_name = g.user_name)
