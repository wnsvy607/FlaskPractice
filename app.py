from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/file_upload',methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return '파일이 저장되었습니다'
    else:
        return render_template('file_upload.html')
    return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=True, port=9999)