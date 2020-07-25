from flask import Blueprint, url_for

app = Blueprint('dateNow', __name__)
@app.route('/date')
def index():
    return url_for('hello')
    # return 'Date Now!'