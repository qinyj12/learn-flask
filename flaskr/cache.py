from werkzeug.contrib.cache import SimpleCache
from functools import wraps
from flask import request, Blueprint

app = Blueprint('cache', __name__)
cache = SimpleCache()

def cached(timeout=60, key='view_%s'):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache_key = key % request.path
            value = cache.get(cache_key)
            if value is None:
                value = f(*args, **kwargs)
                cache.set(cache_key, value, timeout=timeout)
            return value
        return decorated_function
    return decorator

@app.route('/cache')
@cached()
def hello():
    import sys, time
    time_now = time.strftime('%H:%M:%S')
    print(time_now, file=sys.stderr)
    return time.strftime('%H:%M:%S')