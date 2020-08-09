from flask import Blueprint, abort
from flask_restful import Resource, Api, reqparse

app = Blueprint('restful', __name__, url_prefix='/rest')
api = Api(app)

# 这是最简单的flask-restful应用
class HelloWorld(Resource):
    # 如果是get方法
    def get(self):
        return {'hello': 'world'}

# 第一个参数就是resource对象，第二个参数就是url路由
api.add_resource(HelloWorld, '/hello')

# 这是一个复杂一些的flask-restful应用
class Todo1(Resource):
    def get(self):
        # 默认的状态码200
        return {'task': 'Hello world'}

class Todo2(Resource):
    def get(self, todo_id):
        # 自定义状态码201
        return {'task': 'Hello ' + str(todo_id)}, 201

class Todo3(Resource):
    def get(self):
        # 自定义状态码201，并且在response header里塞一个自定义的返回头
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

todos = {'1':'one','2':'two'}
# reqparse对象可以通用地获取request的传参，不管是get、post等都可以用reqparse来获得参数
parser = reqparse.RequestParser()
class Todo4(Resource):
    def get(self):
        # 获得参数里面键为todo_id的值，并且要求是string
        parser.add_argument('todo_id', type=str)
        args = parser.parse_args()
        if args['todo_id'] not in todos:
            return {'error': 'out of range'}, 400
        return todos[args['todo_id']]

    def put(self):
        parser.add_argument('task', type=int)
        args = parser.parse_args()
        task = {'task': args['task']}
        return task

# 加载资源，并且自定义endpoint。endpoint是视图函数的索引。如果不自定义的话，endpoint默认值就是小写的视图函数名，比如todo1。
api.add_resource(Todo1, '/another', '/todo1', endpoint = 'todo_ep')
api.add_resource(Todo2, '/todo2/<int:todo_id>', endpoint = 'todo_ep2')
api.add_resource(Todo3, '/todo3')
api.add_resource(Todo4, '/todo4')
