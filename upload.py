from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__,template_folder='myhtml')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def uploadfile():
    return render_template('formupload.html')

@app.route('/uploader',methods = ['POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        name = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
        return '<h3> File Berhasil Diupload </h3>'

if __name__ == '__main__':
    app.run()