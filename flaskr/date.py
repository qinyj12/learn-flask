from flask import Blueprint

app_date = Blueprint('dateNow', __name__)
@app_date.route('/data')
def index():
    return 'Date Now!'