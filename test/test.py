# 做一个一旦函数运行错误就主动报错的装饰器，不要被动等待函数出错
from functools import wraps

def catch_error(func):
    @wraps(func)
    def inner(*args, **kargs):
        try:
            return func(*args, **kargs)
        except Exception as e:
            return e
    return inner

@catch_error
def index():
    return 1/0

print(index())