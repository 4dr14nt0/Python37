from flask import Flask,redirect,url_for,request
app = Flask(__name__)

@app.route('/submit',methods = ['POST','GET'])
def submit():
    if request.method == 'POST':
        nama = request.form['nama']
        return redirect(url_for('tampilnama',nama1=nama))
    else : 
        nama = request.args.get('nama')
        return redirect(url_for('tampilnama',nama1=nama))

@app.route('/tampilnama/<nama1>')
def tampilnama(nama1):
    return 'Selamat Datang : %s ' %nama1
if __name__ == '__main__':
    app.run()