# 是否开启debug模式
DEBUG = True
# 存放上传文件的目录
UPLOAD_FOLDER = 'uploads/'
# 缓存对象使用的类型
CACHE_TYPE = "simple"
# 缓存默认的过期时间
CACHE_DEFAULT_TIMEOUT = 5
# session的秘钥
# SECRET_KEY = 'abc'
# session的过期时间，整数表示秒，也可以用datetime.timedelta对象
PERMANENT_SESSION_LIFETIME = 5
# 这是session跨域要设置的，有的浏览器用不着
SESSION_COOKIE_SECURE = True
# session的跨域
SESSION_COOKIE_SAMESITE = None