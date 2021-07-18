from flask import Flask, render_template, request
app = Flask(__name__,template_folder='myhtml')

@app.route('/')
def index():
    return render_template('myform.html')

@app.route('/calculate',methods = ['POST'])
def calculate():
    if request.method =='POST':
        result = request.form
        karyawan = {
            'nama' : request.form['nama'],
            'gapok' : int(request.form['gapok']),
            'tunjangan' : int(request.form['tunjangan']),
            'potongan' : int(request.form['potongan']),
            'thp': (int(request.form['gapok']) + int(request.form['tunjangan']) - int(request.form['potongan']))
        }
        return render_template('thpresult.html',data = karyawan)

if __name__ == '__main__':
    app.run()
