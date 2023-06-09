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

# Home
@app.route('/')
def home():
	writerlist = (session.get('writerlist'))
	return render_template('home.html', writerlist=writerlist)

# Log Screenplay
@app.route('/logscreenplay')
def logscreenplay():
	return render_template('logscreenplay.html')	

@app.route('/savelog', methods=['POST'])
def logscreenplaysave():
	title = request.form['title']
	name = request.form['name']
	genre = request.form['genre']
	rating = request.form['rating']
	produced = request.form['produced']
	year = request.form['year']
	logline = request.form['logline']
	synopsis = request.form['synopsis']
	creationdate = date.today()
	import sqlite3
	connection = sqlite3.connect("theWriterList.db")
	cursor = connection.cursor()
	cursor.execute('INSERT INTO screenplays \
		(title, name, genre, rating, produced, year, logline, synopsis, \
			creationdate) values (?, ?, ?, ?, ?, ?, ?, ?, ?)', (title, name,\
			 genre, rating, produced, year, logline, synopsis, creationdate))
	blank = ''
	cursor.execute('INSERT OR IGNORE INTO writers (name, credits) VALUES (?, ?)'\
		, (name, blank))
	cursor.execute('SELECT credits FROM writers WHERE name == ?', (name,))
	old = cursor.fetchone()
	oldcredits = ''.join(old)
	credits = oldcredits + title + ", " 
	cursor.execute('UPDATE writers SET credits = ? WHERE name = ?', (credits, \
		name,))
	connection.commit()
	return render_template('home.html')


#View Library
@app.route('/viewlibrary/')
def viewlibrary():
	import sqlite3
	connection = sqlite3.connect("theWriterList.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM screenplays")
	rows = cursor.fetchall();
	return render_template('viewlibrary.html', rows=rows)

# View individual record and add notes.
@app.route('/viewrecord/<ID>')
def viewrecord(ID):
	userid = ID
	import sqlite3
	connection = sqlite3.connect("theWriterList.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM screenplays WHERE ID = ?", (userid,))
	rows = cursor.fetchall()
	cursor.execute("SELECT * FROM messages WHERE ID = ?", (userid,))
	m = cursor.fetchall()
	for row in rows:
		print(row['name'])
	formatname = (row['name']).replace(" ", "_")
	print("Hello " + formatname)
	return render_template('viewrecord.html', rows=rows, m=m, formatname=formatname)

@app.route('/newnote/<ID>', methods=['POST'])
def newnote(ID):
	userid = ID
	entrydate = date.today()
	message = request.form['message']
	import sqlite3
	connection = sqlite3.connect("theWriterList.db")
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
	connection = sqlite3.connect("theWriterList.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM screenplays WHERE ID = ?", (userid,))
	rows = cursor.fetchall()
	return render_template('editrecord.html', rows=rows, userid=userid)

@app.route('/updaterecord/<ID>', methods=['POST'])
def updaterecord(ID):
	userid = (ID)
	import sqlite3
	connection = sqlite3.connect("theWriterList.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	title = request.form['title']
	name = request.form['name']
	genre = request.form['genre']
	rating = request.form['rating']
	year = request.form['year']
	logline = request.form['logline']
	synopsis = request.form['synopsis']
	cursor.execute("UPDATE screenplays SET title = ?, name = ?, genre = ?, \
		rating = ?, year = ?, logline = ?, synopsis = ? WHERE ID = ?", 
		(title, name, genre, rating, year, logline, synopsis, ID))
	connection.commit()
	site = "/viewrecord/" + (userid)
	return redirect(site)

# Search:
@app.route('/searchlibrary')
def searchlibary():
	return render_template('searchlibrary.html')

@app.route('/titlesearch', methods=['POST'])
def titlesearch():
	#searchtitle = request.form['title']
	searchtitle = "%" + (request.form['search']) + "%"
	print(searchtitle)
	import sqlite3
	connection = sqlite3.connect("theWriterList.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM screenplays WHERE title LIKE ?", (searchtitle,))
	rows = cursor.fetchall()
	return render_template('searchresults.html', rows=rows)

@app.route('/namesearch', methods=['POST'])
def writerfirstsearch():
	#searchtitle = request.form['title']
	searchtitle = "%" + (request.form['search']) + "%"
	print(searchtitle)
	import sqlite3
	connection = sqlite3.connect("theWriterList.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM screenplays WHERE writerfirst LIKE ?", 
		(searchtitle,))
	rows = cursor.fetchall()
	return render_template('searchresults.html', rows=rows)

@app.route('/loglinesearch', methods=['POST'])
def loglinesearch():
	#searchtitle = request.form['title']
	searchtitle = "%" + (request.form['search']) + "%"
	print(searchtitle)
	import sqlite3
	connection = sqlite3.connect("theWriterList.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM screenplays WHERE logline LIKE ?", \
		(searchtitle,))
	rows = cursor.fetchall()
	return render_template('searchresults.html', rows=rows)


@app.route('/synopsissearch', methods=['POST'])
def synopsissearch():
	#searchtitle = request.form['title']
	searchtitle = "%" + (request.form['search']) + "%"
	print(searchtitle)
	import sqlite3
	connection = sqlite3.connect("theWriterList.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM screenplays WHERE synopsis LIKE ?", \
		(searchtitle,))
	rows = cursor.fetchall()
	return render_template('searchresults.html', rows=rows)

@app.route('/genresearch', methods=['POST'])
def genresearch():
	#searchtitle = request.form['title']
	searchtitle = "%" + (request.form['search']) + "%"
	print(searchtitle)
	import sqlite3
	connection = sqlite3.connect("theWriterList.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM screenplays WHERE genre LIKE ?", (searchtitle,))
	rows = cursor.fetchall()
	return render_template('searchresults.html', rows=rows)
# End Search

# Writer's List\
@app.route('/home/makelist')
def makelist():
	return render_template('makelist.html')


@app.route('/createlist/', methods=['POST'])
def creatlist():
	listname = (request.form['listname'])
	updatename = listname.replace(" ", "_")
	import sqlite3
# Add Table to writerlists.db
	wlconnection = sqlite3.connect("writerlists.db")
	wlcursor = wlconnection.cursor()
	wlcursor.execute('''CREATE TABLE IF NOT EXISTS tablename 
		(ID integer, writerfirst text, writerlast text, title text, 
			agent text, available text)''')
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
	site = '/currentlist/' + writerlist
	return redirect(site)

@app.route('/currentlist/<listname>')
def currentlist(listname):
	table = listname
	import sqlite3
	wlconnection = sqlite3.connect("writerlists.db")
	wlconnection.row_factory = sqlite3.Row
	wlcursor = wlconnection.cursor()
	wlcursor.execute("SELECT * FROM %s" %table)
	rows = wlcursor.fetchall()
	for row in rows:
		print('mark')
	return render_template('currentlist.html', rows=rows)

@app.route('/viewwriter/<name>')
def viewwriter(name):
	import sqlite3
	connection = sqlite3.connect("theWriterList.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	name = name.replace("_", " ")
	print('-----')
	print(name)
	cursor.execute("SELECT * FROM writers WHERE name LIKE ?", (name,))
	rows = cursor.fetchall()
	cursor.execute("SELECT * FROM screenplays WHERE name LIKE ?", (name,))
	screenplays = cursor.fetchall()
	return render_template('viewwriter.html', rows=rows, screenplays=screenplays)

@app.route('/addtowriterlist', methods=['POST'])
def addtowriterlist():
	import sqlite3
	listname = (session.get('writerlist'))
	print("-----")
	print(listname)
	writerfirst = request.form['writerfirst']
	writerlast = request.form['writerlast']
	title = request.form['credits']
	wlconnection = sqlite3.connect("writerlists.db")
	wlcursor = wlconnection.cursor()
	wlcursor.execute("INSERT INTO %s (writerfirst, writerlast, title) VALUES \
		(?, ?, ?)" %(listname), (writerfirst, writerlast, title)) 
	wlconnection.commit()
	site = '/currentlist/' + listname
	return redirect(site)

# Close Flask
if __name__ == '__main__':
   app.run(debug = True)