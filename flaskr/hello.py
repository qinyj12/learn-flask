from flask import Blueprint, request, flash
from .decoration import ban_get
import sys

app_hello = Blueprint('hello', __name__)
@app_hello.route('/hello')
# @ban_get
def index():
    # return 'Hello world!'
    return request.method