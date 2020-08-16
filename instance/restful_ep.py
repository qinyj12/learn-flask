# 这是一个用来测试restful中的endpoint的视图函数
from flask import Blueprint, url_for, redirect

app = Blueprint('restful_ep', __name__, url_prefix='/restep')

# 这是普通蓝图route的实现
@app.route('/route/<int:todo_id>')
def index(todo_id):
    # 因为restful.py中的视图函数手动指定了endpoint=todo_ep2，所以url_for也要指明是todo_ep2
    # 如果不手动指定endpoint的话,那么那个视图函数的endpoint就是函数名的小写。比如原来函数名是Todo2，那url_for就要指明是todo2
    return redirect(url_for('restful.todo_ep2', todo_id = todo_id))

# 这是flask-restful的实现
from flask_restful import Resource, Api
api = Api(app)
class RestfulEp(Resource):
    def get(self, todo_id):
        return redirect(url_for('restful.todo_ep2', todo_id = todo_id))

api.add_resource(RestfulEp, '/resource/<int:todo_id>')