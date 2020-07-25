from flask import Blueprint, g, url_for, current_app

lang_bp = Blueprint('lang', __name__, url_prefix='/<lang_code>')

# url_value_preprocessor所装饰的函数，会在视图函数被调用之前执行、url路径被预处理时执行。
# 他所传入的第二个参数保存了当前请求url上所有参数的值。
#如果请求的url是'/zh/path'，那第二个参数就是{'lang_code': 'zh'}
@lang_bp.url_value_preprocessor
def get_lang_code_from_url(endpoint, view_args):
    import sys
    print('view_args: ' + str(view_args), file=sys.stderr)
    g.lang_code = view_args.pop('lang_code')
    

# url_defaultes装饰的函数会在每次调用url_for时执行
# @lang_bp.url_defaults
# def add_language_code(endpoint, values):
#     values.setdefault('lang_code', g.lang_code)

@lang_bp.route('/')
def index():
    return '<h1>Index of language %s</h1>' % g.lang_code

@lang_bp.route('/path')
def path():
    # 因为url_defaults的存在，所以不用再写成url_for('.index', lang_code=g.lang_code)
    # return '<h1>Language base URL is %s</h1>' % url_for('.index')
    return '<h1>Language base URL is %s</h1>' % url_for('.index', lang_code=g.lang_code)