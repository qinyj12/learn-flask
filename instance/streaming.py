from flask import Response, Blueprint

app = Blueprint('streaming', __name__)

# @app.route('/large.csv')
# def generate_large_csv():
#     def generate():
#         for row in iter_all_rows():
#             yield ','.join(row) + '\n'
#     return Response(generate(), mimetype='text/csv')