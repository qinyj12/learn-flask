from functools import wraps
import sys

from flask.helpers import url_for

def ensure_running(func):
    @wraps(func)
    def inner(*args, **kargs):
        print('Ensuring Running: ' + func.__name__, file = sys.stderr)
        return func(*args, **kargs)
    return inner