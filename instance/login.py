from flask import Blueprint, render_template, request

app = Blueprint('login', __name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return request.form['username']
    return render_template('login.html')