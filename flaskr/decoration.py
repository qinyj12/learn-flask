from datetime import date
from functools import wraps
import sys, datetime

from flask import request, abort

def ban_get(func):
    @wraps(func)
    def inner():
        print(datetime.datetime.now(),file=sys.stderr)
        if request.method != 'GET':
            return func()
        else:
            return '123'
    return inner
