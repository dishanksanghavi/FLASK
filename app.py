import pandas as pd
from flask import Flask,render_template, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
	try:
		if request.method == 'GET':
			return "Login via the login Form"
		if request.method == 'POST':
			fname = request.form['fname']
			lname = request.form['lname']
			address = request.form['address']
			age = request.form['age']
			schoolID = request.form['schoolID']
			phnumber = request.form['phnumber']
			cursor = mysql.connection.cursor()
			cursor.execute('''INSERT INTO data_table (fname,lname,address,age,schoolID,phnumber) VALUES (%s,%s,%s,%s,%s,%s)''',(fname,lname,address,age,schoolID,phnumber))
			mysql.connection.commit()
			cursor.close()
			return f"Done"
	except Exception as e:
		return(str(e))

@app.route('/find')
def find():
    return render_template('find.html')

@app.route('/select_table', methods = ['POST'])
def select_table():
	try:
		fname = request.form['fname']
		cursor = mysql.connection.cursor()
		sql = "SELECT * FROM data_table WHERE fname = %s"
		adr = (fname, )
		cursor.execute(sql, adr)
		rows = cursor.fetchall()
		return render_template('show.html',rows=rows)
	except Exception as e:
		return(str(e))
	
app.run(host='localhost', port=5000)