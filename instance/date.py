from flask import Blueprint

app = Blueprint('dateNow', __name__)
@app.route('/date/<dater_name>')
def index(dater_name):
    return 'let\'s date now!! %s' % dater_name