import os
from flask import flash, request, redirect, url_for, Blueprint, current_app
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Blueprint('upload', __name__)

from .decoration import ensure_running
@ensure_running
def allowed_file(filename):
    result = '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    import sys
    print('allowed_file: ' + str(result), file = sys.stderr)
    return result

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        import sys
        # ImmutableMultiDict([('file', <FileStorage: 'dog.jpg' ('image/jpeg')>)])
        print('request.files: ' + str(request.files), file = sys.stderr)

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        # <FileStorage: 'dog.jpg' ('image/jpeg')>
        file = request.files['file']
        import sys
        print('request.files[file]: ' + str(file), file = sys.stderr)

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('.upload_file',filename=filename))

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
    </form>
    '''