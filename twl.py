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

# Search:
@app.route('/home/searchlibrary')
def searchlibary():
	return render_template('searchlibrary.html')

@app.route('/titlesearch', methods=['POST'])
def titlesearch():
	#searchtitle = request.form['title']
	searchtitle = "%" + (request.form['search']) + "%"
	print(searchtitle)
	import sqlite3
	connection = sqlite3.connect("twl.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM library WHERE title LIKE ?", (searchtitle,))
	rows = cursor.fetchall()
	return render_template('searchresults.html', rows=rows)

@app.route('/writerfirstsearch', methods=['POST'])
def writerfirstsearch():
	#searchtitle = request.form['title']
	searchtitle = "%" + (request.form['search']) + "%"
	print(searchtitle)
	import sqlite3
	connection = sqlite3.connect("twl.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM library WHERE writerfirst LIKE ?", 
		(searchtitle,))
	rows = cursor.fetchall()
	return render_template('searchresults.html', rows=rows)

@app.route('/writerlastsearch', methods=['POST'])
def writerlastsearch():
	#searchtitle = request.form['title']
	searchtitle = "%" + (request.form['search']) + "%"
	print(searchtitle)
	import sqlite3
	connection = sqlite3.connect("twl.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM library WHERE writerlast LIKE ?", 
		(searchtitle,))
	rows = cursor.fetchall()
	return render_template('searchresults.html', rows=rows)

@app.route('/loglinesearch', methods=['POST'])
def loglinesearch():
	#searchtitle = request.form['title']
	searchtitle = "%" + (request.form['search']) + "%"
	print(searchtitle)
	import sqlite3
	connection = sqlite3.connect("twl.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM library WHERE logline LIKE ?", (searchtitle,))
	rows = cursor.fetchall()
	return render_template('searchresults.html', rows=rows)


@app.route('/synopsissearch', methods=['POST'])
def synopsissearch():
	#searchtitle = request.form['title']
	searchtitle = "%" + (request.form['search']) + "%"
	print(searchtitle)
	import sqlite3
	connection = sqlite3.connect("twl.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM library WHERE synopsis LIKE ?", (searchtitle,))
	rows = cursor.fetchall()
	return render_template('searchresults.html', rows=rows)

@app.route('/genresearch', methods=['POST'])
def genresearch():
	#searchtitle = request.form['title']
	searchtitle = "%" + (request.form['search']) + "%"
	print(searchtitle)
	import sqlite3
	connection = sqlite3.connect("twl.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM library WHERE genre LIKE ?", (searchtitle,))
	rows = cursor.fetchall()
	return render_template('searchresults.html', rows=rows)
# End Search

# Writer's List
@app.route('/home/makelist')
def makelist():
	return render_template('makelist.html')


@app.route('/createlist/', methods=['POST'])
def creatlist():
	updatename = [request.form['listname']]
	import sqlite3
# Add Table to writerlists.db
	wlconnection = sqlite3.connect("writerlists.db")
	wlcursor = wlconnection.cursor()
	wlcursor.execute('''CREATE TABLE IF NOT EXISTS tablename 
		(ID integer, writerfirst text, writerlast text, title text)''')
	wlconnection.commit()
	wlcursor.execute("ALTER TABLE tablename RENAME TO %s" %updatename)
	wlconnection.commit()
	return redirect('/listlists')

@app.route('/listlists')
def listlists():
	import sqlite3
	wlconnection = sqlite3.connect("writerlists.db")
	wlcursor = wlconnection.cursor()
	wlconnection.row_factory = sqlite3.Row
	wlcursor.execute("SELECT name FROM sqlite_schema WHERE type ='table' \
		AND name NOT LIKE 'sqlite_%';")
	items = wlcursor.fetchall()
	for item in items:
		print(item)
	return render_template('listlists.html', items=items)

@app.route('/setlistvariable/<listname>')
def setlistvariable(listname):
	session['writerlist']=listname
	writerlist=session.get('writerlist')
	print('-----------')
	print(writerlist)
	return 'ok'



@app.route('/addtolist/<ID>')
def addtolist(ID):
	userid = ID
	import sqlite3
	connection = sqlite3.connect("twl.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM library WHERE ID = ?", (userid,))
	rows = cursor.fetchall()
	for row in rows:
		print(row[0])
	listname = ['Anal']
	#print(listname)
	writerfirst = (row['writerfirst'])
	writerlast = (row['writerlast'])
	title = (row['title'])
	wlconnection = sqlite3.connect("writerlists.db")
	wlcursor = wlconnection.cursor()
	wlcursor.execute("INSERT INTO %s (writerfirst, writerlast, title) VALUES \
		(?, ?, ?)" %listname, (writerfirst, writerlast, title)) 
	wlconnection.commit()
	return "Hi"

@app.route('/currentlist/<ID>')
def currentlist(ID):
	table = ['Anal']
	import sqlite3
	wlconnection = sqlite3.connect("writerlists.db")
	wlconnection.row_factory = sqlite3.Row
	wlcursor = wlconnection.cursor()
	wlcursor.execute("SELECT * FROM %s" %table)
	rows = wlcursor.fetchall()
	for row in rows:
		print(row[0])
	#writerfirst = (row['writerfirst'])
	#writerlast = (row['writerlast'])
	#title = (row['title'])
	#print(writerfirst)
	return render_template('currentlist.html', rows=rows)



# Close Flask
if __name__ == '__main__':
   app.run(debug = True)