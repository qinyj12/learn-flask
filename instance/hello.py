from flask import Blueprint, g, url_for, current_app
from .decoration import ensure_running
from .bye import test

app_hello = Blueprint('hello', __name__)

@app_hello.route('/hello', endpoint='qq')
def hello():
    g.temp = str(current_app.url_map)
    return test()
    # return 'Hello World!'