from flask import Flask,render_template
app = Flask(__name__,template_folder='myhtml')

@app.route('/')
def index():
    return'<html><h1>Welcome to Application</h1></html>'

@app.route('/hello')
def hello_name():
    return render_template('hello.html')

@app.route('/kirimdata/<text>')
def kirimdata(text):
    return render_template("kirimdata.html",data=text)

@app.route('/detailmahasiswa')
def detailmahasiswa():
    mahasiswa = [{
        'nik':212121,
        'nama':'sentosa',
        'nilai':100,
        'JK':'Pria'    
    }]
    return render_template("detailmahasiswa.html",data=mahasiswa)

if __name__ == '__main__':
    app.run()