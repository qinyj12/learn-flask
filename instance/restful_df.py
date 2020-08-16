# 这是一个用来测试data formatting的视图函数
from flask import Blueprint, abort
from flask_restful import fields, marshal_with, Resource, Api, reqparse

app = Blueprint('restful_df', __name__, url_prefix = '/restdf')
api = Api(app)

# 这是官方文档给的案例
resource_fields = {
    # 这里虽然在资源路由里传了参（todo_id），格式化数据里却并没有这个参数，但并不会报错
    # 'todo_id': fields.String,
    'task': fields.String,
    'uri': fields.Url('restful.todo_ep'),
    # 这里虽然在格式化数据里定义了（rest），但资源路由里并没有传参，最终response时会返回null
    'rest': fields.String
}
class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task
        # This field will not be sent in the response
        self.status = 'active'
class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')
api.add_resource(Todo, '/todo')
# 这是一个自定义fields的案例
# 先定义一个gender类，要求接收的参数不是male就是female，否则调用abort
class Gender(fields.Raw):
    def format(self, value):
        return value if value in {'male', 'female'} else abort(500)

# 然后自定义一个格式化的数据，这个数据就是返回给前端的response，这里对response的格式、类型等做了限定：
# 比如id只能是int，如果是str就会报错。
user_fields = {
    'id': fields.Integer,
    # 如果给本fields发送的请求中不含有name（实操下来发现就是name = None），则response默认值unnamed
    'name': fields.String(default = 'unnamed'),
    'nickname': fields.String,
    'gender': Gender,
    # 可以自定义格式化数据
    'greeting': fields.FormattedString('hello {nickname}'),
}

# 这似乎是一个中间件，资源调用这个中间件，然后中间件再去查询fields
class QueryUser(object):
    # 给name参数设置默认值None，这样才能触发fields中的default
    def __init__(self, id, gender, nickname, name = None):
        self.id = id
        self.gender = gender
        self.nickname = nickname
        self.name = name

# 这才是资源本体
class User(Resource):
    # 使用marshal_with装饰器
    @marshal_with(user_fields)
    def get(self, **kwargs):
        # 用reqparse获取request的参数
        parser = reqparse.RequestParser()
        # request的参数id只能是int
        parser.add_argument('id', type = int)
        # 这里尝试获取request的name参数，但最终不会传参给中间件，因为要触发default
        parser.add_argument('name', type = str)
        # choices指定了request的参数必须在什么范围内，比如这里要求gender的值只能是male或者female，否则会触发reqparse的error
        # help是自定义错误信息。如果触发了error的话，那此处的response就是：
        # {"message": {"gender": "Bad choice: femal is not a valid choice"}}
        parser.add_argument('gender', choices = ('male', 'female'), help = 'Bad choice: {error_msg}')
        parser.add_argument('nickname', type = str)
        args = parser.parse_args()
        # 传参给中间件。如果前端参数为空（即没有相应的参数），那args['xxx']的值就是null。如果中间件没有定义默认值，也没有接到资源路由传来的参数，那会报错的。
        return QueryUser(id = args['id'], gender = args['gender'], nickname = args['nickname'], name = args['name'])

api.add_resource(User, '/')