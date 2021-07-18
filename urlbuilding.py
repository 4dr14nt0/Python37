from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def page_admin():
    return 'Welcome Admin'

@app.route('/guest/<name>')
def page_guest(name):
    return 'Welcome back User : '+name

@app.route('/login/<name>')
def login(name):
    if name=='admin':
        return redirect(url_for('page_admin'))
    else:
        return redirect(url_for('page_guest',name=name))

if __name__ == '__main__':
    app.run()