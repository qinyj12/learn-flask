from flask import Blueprint, render_template, request, g, redirect, session
from flask.helpers import url_for
from functools import wraps

app = Blueprint('login', __name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['username']
        # g.user = request.form['username']
        return redirect(url_for('login.admin'))
    session['user'] = 'qinyj12'
    import sys
    print(session['user'], file = sys.stderr)
    return render_template('login.html')

def ensure_login(func):
    @wraps(func)
    def inner(*args, **kargs):
        # 判断g中存不存在'user'这个键
        if 'user' in session:
            import sys
            print('yes', file = sys.stderr)
            g.user = session['user']
            return func(*args, **kargs)
        else:
            import sys
            print('no', file = sys.stderr)
            return redirect(url_for('.login'))
    return inner

@app.route('/admin')
# @ensure_login
def admin():
    return session['user']