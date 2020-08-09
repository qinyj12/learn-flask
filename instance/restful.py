from flask import Blueprint
from flask_restful import Resource, Api, reqparse

app = Blueprint('restful', __name__, url_prefix='/rest')
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('todo_id')
# args = parser.parse_args()

# 一个路由
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/hello')

# 又一个路由
todos = {'1':'one','2':'two'}

class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world'}

class Todo2(Resource):
    def get(self, todo_id):
        # Set the response code to 201
        return {'task': 'Hello ' + str(todo_id)}, 201

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

class Todo4(Resource):
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        todos[todo_id] = task
        return todos[todo_id]

api.add_resource(Todo1, '/another', '/todo1', endpoint = 'todo_ep')
api.add_resource(Todo2, '/todo2/<int:todo_id>', endpoint = 'todo_ep2')
api.add_resource(Todo3, '/todo3')
api.add_resource(Todo4, '/todo4/<todo_id>')
