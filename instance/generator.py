from flask import Blueprint, Response, current_app, stream_with_context
import csv

app = Blueprint('generator', __name__)

@app.route('/generator')
def index():
    def generator():
        import os
        with open(os.path.join(current_app.config['STATIC_PATH'], 'test.csv'), encoding='utf-8') as f:
            f_csv = csv.DictReader(f)
            for row in f_csv:
                yield ' ' + row['updated_at']

    return Response(stream_with_context(generator()), mimetype='text/html')

    # def generator():
    #     i = 0
    #     while i < 5:
    #         yield str(i)
    #         import time
    #         time.sleep(1)
    #         i += 1
    
    # return Response(generator())