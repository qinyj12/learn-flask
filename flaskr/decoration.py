from functools import wraps
import sys

def ensure_running(func):
    @wraps(func)
    def inner(*args, **kargs):
        print('running: ' + func.__name__, file=sys.stderr)
        return func(*args, **kargs)
    return inner