from flask import Flask, render_template, request, url_for, redirect
import pymysql

app = Flask(__name__)
conn= pymysql.connect('localhost','jayadmin','jayeng51','testweb')

@app.route('/')
def Home():
    with conn :
        cur=conn.cursor()
        cur.execute("select * from node1 where ( `id` = (select max(`id`) from `node1`))")
        rows = cur.fetchall()
        print(rows[0][1])
        return render_template('home.html', value1 = rows[0][3], value2 = rows[0][4], value3 = 50, value4 = 50, value5 = 50, value6 = 50)

@app.route('/showdata1')
def data1():
    return render_template('showdata1.html',no_page = 1)

@app.route('/showdata2')
def data2():
    return render_template('showdata2.html',no_page = 2)

@app.route('/showdata3')
def data3():
    return render_template('showdata3.html',no_page = 3)

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