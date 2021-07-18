from flask import Flask,render_template,request,url_for,redirect
from flask_mysqldb import MySQL

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Buat Koneksi ke MySQL (disesuaikan)
app = Flask(__name__,template_folder='myhtml')
app.config['MYSQL_HOST'] = '128.199.137.36'
app.config['MYSQL_USER'] = 'adam'
app.config['MYSQL_PASSWORD'] = 'Inixindo@2020'
app.config['MYSQL_DB'] = 'db_training'
mysql = MySQL(app)

@app.route('/')
def list():
    cur = mysql.connection.cursor()
    query = "SELECT * FROM anggota"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return render_template('list.html',data=data)

@app.route('/addanggota',methods=['POST'])
def add():
    if request.method == 'POST':
        nik = request.form['nik']
        nama = request.form['nama']
        telp = request.form['telp']
        usia = request.form['usia']
        tgllahir = request.form['tgllahir']
        alamat = request.form['alamat']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO anggota(nik,nama,tgl_lahir,alamat,telp,usia) VALUES (%s, %s, %s, %s, %s,%s)", (nik,nama,tgllahir,alamat,telp,usia))
        mysql.connection.commit()
        cur.close()
        return 'Success'
    else :
        return 'Failed'

@app.route('/editanggota',methods=['POST'])
def edit():
    if request.method == 'POST':
        id = request.form['edit_id']
        nik = request.form['edit_nik']
        nama = request.form['edit_nama']
        telp = request.form['edit_telp']
        usia = request.form['edit_usia']
        tgllahir = request.form['edit_tgllahir']
        alamat = request.form['edit_alamat']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE anggota SET nik=%s,nama=%s,tgl_lahir=%s,alamat=%s,telp=%s,usia=%s WHERE id=%s", (nik,nama,tgllahir,alamat,telp,usia,id))
        mysql.connection.commit()
        cur.close()
        return 'Success'
    else :
        return 'Failed'

@app.route('/deleteanggota',methods=['GET'])
def delete():
    if request.method == 'GET':
        id = request.args.get('id')
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM anggota WHERE id=%s",[id])
        mysql.connection.commit()
        cur.close()
        return 'Success'
    else :
        return 'Failed'

@app.route('/dataframe',methods=['GET'])
def dataframe():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        query = "SELECT * FROM anggota"
        cur.execute(query)
        data = cur.fetchall()
        df = pd.DataFrame(data)
        df_head = df.head(5)
        return render_template('dataframe.html',tables=[df_head.to_html(classes='data')])

# @app.route('/ploting',methods=['GET'])
# def ploting():
#     if request.method == 'GET':
#         left = [1, 2, 3, 4, 5]
#         # heights of bars
#         height = [10, 24, 36, 40, 5]
#         # labels for bars
#         tick_label = ['one', 'two', 'three', 'four', 'five']
#         # plotting a bar chart
#         plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])

#         # naming the y-axis
#         plt.ylabel('y - axis')
#         # naming the x-axis
#         plt.xlabel('x - axis')
#         # plot title
#         plt.title('My bar chart!')

#         plt.savefig('plot.png')

#         return render_template('plot.html', url='plot.png')


if __name__ == '__main__':
    app.run()
