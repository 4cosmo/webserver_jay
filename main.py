from flask import Flask, render_template, request, url_for, redirect
import pymysql

app = Flask(__name__)
conn= pymysql.connect('localhost','jayadmin','jayeng51','testweb')

@app.route('/')
def Home():
    with conn :
        cur=conn.cursor()
        cur.execute("select * from node1 where ( `id` = (select max(`id`) from `node1`))")
        rows1 = cur.fetchall()
        cur.execute("select * from node2 where ( `id` = (select max(`id`) from `node2`))")
        rows2 = cur.fetchall()
        cur.execute("select * from node3 where ( `id` = (select max(`id`) from `node3`))")
        rows3 = cur.fetchall()
        return render_template('home.html', value2 = rows1[0][3], value1 = rows1[0][4], value4 = rows2[0][3], value3 = rows2[0][4], value6 = rows3[0][3], value5 = rows3[0][4])

@app.route('/showdata1')
def data1():
    with conn :
        cur=conn.cursor()
        cur.execute("select * from node1 order by id desc limit 200;")
        rows = cur.fetchall()
        return render_template('showdata1.html',no_page = 1, datas = rows)

@app.route('/showdata2')
def data2():
    with conn :
        cur=conn.cursor()
        cur.execute("select * from node2 order by id desc limit 200;")
        rows = cur.fetchall()
        return render_template('showdata1.html',no_page = 1, datas = rows)

@app.route('/showdata3')
def data3():
    with conn :
        cur=conn.cursor()
        cur.execute("select * from node3 order by id desc limit 200;")
        rows = cur.fetchall()
        return render_template('showdata1.html',no_page = 1, datas = rows)

@app.route('/showdata1', methods=['POST'])
def datas1():
    if request.method == "POST" :
        with conn :
            cur=conn.cursor()
            tempLow = request.form['temp_min']
            tempHigh = request.form['temp_max']
            humitLow = request.form['humid_min']
            humitHigh = request.form['humid_max']
            if (tempHigh < tempLow or humitHigh < humitLow) :
                return render_template('showdata1.html',no_page = 1)
            cur.execute("select * from node1 WHERE (`temp` BETWEEN %s AND %s) AND (`humit` BETWEEN %s AND %s)",(tempLow, tempHigh, humitLow, humitHigh))
            rows = cur.fetchall()
            print(rows)
            return render_template('showdata1.html',no_page = 1, datas = rows)
    else :
        return render_template('showdata1.html',no_page = 1)

@app.route('/showdata2', methods=['POST'])
def datas2():
    if request.method == "POST" :
        with conn :
            cur=conn.cursor()
            tempLow = request.form['temp_min']
            tempHigh = request.form['temp_max']
            humitLow = request.form['humid_min']
            humitHigh = request.form['humid_max']
            if (tempHigh < tempLow or humitHigh < humitLow) :
                return render_template('showdata2.html',no_page = 1)
            cur.execute("select * from node2 WHERE (`temp` BETWEEN %s AND %s) AND (`humit` BETWEEN %s AND %s)",(tempLow, tempHigh, humitLow, humitHigh))
            rows = cur.fetchall()
            print(rows)
            return render_template('showdata2.html',no_page = 2, datas = rows)
    else :
        return render_template('showdata2.html',no_page = 2)

@app.route('/showdata3', methods=['POST'])
def datas3():
    if request.method == "POST" :
        with conn :
            cur=conn.cursor()
            tempLow = request.form['temp_min']
            tempHigh = request.form['temp_max']
            humitLow = request.form['humid_min']
            humitHigh = request.form['humid_max']
            if (tempHigh < tempLow or humitHigh < humitLow) :
                return render_template('showdata3.html',no_page = 3)
            cur.execute("select * from node3 WHERE (`temp` BETWEEN %s AND %s) AND (`humit` BETWEEN %s AND %s)",(tempLow, tempHigh, humitLow, humitHigh))
            rows = cur.fetchall()
            print(rows)
            return render_template('showdata3.html',no_page = 3, datas = rows)
    else :
        return render_template('showdata3.html',no_page = 3)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4589)