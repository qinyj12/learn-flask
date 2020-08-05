from .cache import cache
from flask import Blueprint
import time

app = Blueprint('cache', __name__)

@app.route('/cache')
# 把这个视图函数加入cache，并且3秒后过期
@cache.cached(timeout = 3)
def cache():
    return time.strftime('%H:%M:%S')