from flask import Blueprint, g, url_for, current_app

lang_bp = Blueprint('lang', __name__, url_prefix='/lang/<lang_code>')

# url_value_preprocessor所装饰的函数，会在视图函数被调用之前执行、url路径被预处理时执行
# 他所传入的第二个参数保存了当前请求url上参数的值，仅限在<>内的动态参数，比如本蓝图中的<lang_code>
#如果请求的url是'/zh/path'，那第二个参数就是{'lang_code': 'zh'}，也就是view_arges的参数
@lang_bp.url_value_preprocessor
def get_lang_code_from_url(endpoint, view_args):
    g.lang_code = view_args.pop('lang_code')

# url_defaultes装饰的函数会在每次调用url_for时执行，可以设置url的默认参数（比如这个蓝图的lang_code），保存在这个函数的第二个参数上
# 有了这个url_defaultes，就不用每次在url_for()里面加入参数了
@lang_bp.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

@lang_bp.route('/')
def index():
    return '<h1>Index of language %s</h1>' % g.lang_code

@lang_bp.route('/path')
def path():
    # 因为url_defaults的存在，所以不用再写成url_for('.index', lang_code=g.lang_code)
    return '<h1>Language base URL is %s</h1>' % url_for('.index')
    # return '<h1>Language base URL is %s</h1>' % url_for('.index', lang_code=g.lang_code)