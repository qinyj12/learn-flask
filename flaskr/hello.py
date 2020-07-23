from flask import Blueprint, request, flash
import sys

app_hello = Blueprint('hello', __name__)
@app_hello.route('/hello')
def index():
    # return 'Hello world!'
    return request.method