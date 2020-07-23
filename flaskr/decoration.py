from functools import wraps
import sys

def ensure_running(func):
    @wraps(func)
    def inner():
        print('running: ' + func.__name__, file=sys.stderr)
        return func()
    return inner