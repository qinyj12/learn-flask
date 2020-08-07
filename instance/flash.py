from flask import Blueprint, flash, redirect, render_template, request, url_for

app = Blueprint('flash', __name__, url_prefix='/flash')

@app.route('/')
def index():
    return render_template('flash_index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('.index'))
    return render_template('flash_login.html', error=error)