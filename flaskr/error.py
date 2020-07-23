from flask import Blueprint, render_template
from .decoration import ensure_running

app_error = Blueprint('error', __name__)

@app_error.app_errorhandler(500)
@ensure_running
def page_not_found(error):
    return render_template('500.html'), 500