from flask import Flask
from flask import send_file
from flask import render_template
from flask import request
import os
from flask import session
import datetime
from datetime import datetime
from datetime import date
from datetime import time 
from flask import redirect


app = Flask(__name__)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'
# End of opening

# setup sqlite

def sqlconnect():
	import sqlite3
	connection = sqlite3.connect("twl.db")
	cursor = connection.cursor()
# end sqlite setup

# Home
@app.route('/home/')
def home():
	return render_template('home.html')

# Log Screenplay
@app.route('/home/logscreenplay/')
def logscreenplay():
	return render_template('logscreenplay.html')	

@app.route('/savelog', methods=['POST'])
def logscreenplaysave():
	title = request.form['title']
	writerfirst = request.form['writerfirst']
	writerlast = request.form['writerlast']
	genre = request.form['genre']
	starrating = request.form['starrating']
	logline = request.form['logline']
	synopsis = request.form['synopsis']
	creationdate = date.today()
	import sqlite3
	connection = sqlite3.connect("twl.db")
	cursor = connection.cursor()
	cursor.execute('INSERT INTO library \
		(title, writerfirst, writerlast, genre, starrating, logline, synopsis, \
			creationdate) values (?, ?, ?, ?, ?, ?, ?, ?)', (title, writerfirst, \
			writerlast, genre, starrating, logline, synopsis, creationdate))
	connection.commit()
	return render_template('home.html')


#View Library
@app.route('/home/viewlibrary/')
def viewlibrary():
	import sqlite3
	connection = sqlite3.connect("twl.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM library")
	rows = cursor.fetchall();
	return render_template('viewlibrary.html', rows=rows)

# View individual record and add notes.
@app.route('/viewrecord/<ID>')
def viewrecord(ID):
	userid = ID
	import sqlite3
	connection = sqlite3.connect("twl.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM library WHERE ID = ?", (userid,))
	rows = cursor.fetchall()
	cursor.execute("SELECT * FROM messages WHERE ID = ?", (userid,))
	m = cursor.fetchall()
	return render_template('viewrecord.html', rows=rows, m=m)

@app.route('/newnote/<ID>', methods=['POST'])
def newnote(ID):
	userid = ID
	entrydate = date.today()
	message = request.form['message']
	import sqlite3
	connection = sqlite3.connect("twl.db")
	cursor = connection.cursor()
	cursor.execute('INSERT INTO messages (ID, entrydate, message) VALUES \
		(?, ?,?)', (ID, entrydate, message))
	connection.commit()
	site = "/viewrecord/" + (userid)
	return redirect(site)

# Edit records
@app.route('/editrecord/<ID>')
def editrecord(ID):
	userid = ID
	import sqlite3
	connection = sqlite3.connect("twl.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM library WHERE ID = ?", (userid,))
	rows = cursor.fetchall()
	return render_template('editrecord.html', rows=rows, userid=userid)

@app.route('/updaterecord/<ID>', methods=['POST'])
def updaterecord(ID):
	userid = (ID)
	import sqlite3
	connection = sqlite3.connect("twl.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	newtitle = request.form['title']
	newwriterfirst = request.form['writerfirst']
	newwriterlast = request.form['writerlast']
	newlogline = request.form['logline']
	newsynopsis = request.form['synopsis']
	cursor.execute("UPDATE library SET title = ?, writerfirst = ?, \
		writerlast = ?, logline = ?, synopsis = ? WHERE ID = ?", \
		(newtitle, newwriterfirst, newwriterlast, newlogline, newsynopsis, userid))
	connection.commit()
	site = "/viewrecord/" + (userid)
	return redirect(site)

@app.route('/home/searchlibrary')
def searchlibary():
	return render_template('searchlibrary.html')

@app.route('/titlesearch', methods=['POST'])
def search():
	searchtitle = request.form['title']
	import sqlite3
	connection = sqlite3.connect("twl.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	#cursor.execute("SELECT * FROM library WHERE title = ?", [title])
	#rows = cursor.fetchall()
	#cursor.execute("SELECT * FROM library WHERE instr(title, ?) > 0", [searchtitle])
	cursor.execute("SELECT * FROM library WHERE title LIKE '%searchtitle%'")
	rows = cursor.fetchall()
	return render_template('searchresults.html', rows=rows)














# Close Flask
if __name__ == '__main__':
   app.run(debug = True)