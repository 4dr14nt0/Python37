from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/show/<name>')
def show(name):
    return 'Hallo ' + name
app.run(port=5000, host='0.0.0.0')