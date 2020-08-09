from flask import Blueprint, request
from flask_restful import Resource, Api

app = Blueprint('restful', __name__, url_prefix='/rest')
api = Api(app)

# 一个路由
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/hello')

# 又一个路由
todos = {'1':'one','2':'two'}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')