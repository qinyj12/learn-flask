from flask import Blueprint, render_template, request, g, redirect, session
from flask.helpers import url_for
from functools import wraps

app = Blueprint('login', __name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['username']
        # url_for中的next对象会存在于request.args，比如https://127.0.0.1:5000/admin?next=Hello&haha=bye
        return redirect(url_for('login.admin', next='Hello', haha='bye'))
    return render_template('login.html')

def ensure_login(func):
    @wraps(func)
    def inner(*args, **kargs):
        # 判断g中存不存在'user'这个键
        if 'user' in session:
            g.user = session['user']
            return func(*args, **kargs)
        else:
            return redirect(url_for('.login'))
    return inner

@app.route('/admin')
@ensure_login
def admin():
    # request.args.get('next')是从url_for中的next拿到的值，比如url_for('login.admin', next='Hello')
    return request.args.get('next') + ' ' + g.user