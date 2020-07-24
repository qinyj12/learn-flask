from flask import Blueprint, abort, g
from .decoration import ensure_running
from .bye import test

app_hello = Blueprint('hello', __name__)
@app_hello.route('/hello')
@ensure_running
def hello():
    # abort(404)
    # g.temp = '123'
    return test('123')
    # return 'Hello World!'