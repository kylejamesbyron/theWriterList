import sqlite3

connection = sqlite3.connect("tester.db")

cursor = connection.cursor()

# To Insert Table:
#cursor.execute("CREATE TABLE media (title TEXT, author TEXT, media TEXT, description TEXT)") 

title = input("title:")
author = input("author:")
media = input("media:")
description = input("description:")

print("Variables:")
print(title)
print(author)
print(media)
print(description)


# To Insert Values
cursor.execute("INSERT INTO media (title, author, media, description) values (?, ?, ?, ?)", 
		(title, author, media, description))
connection.commit()

#To read values
rows = cursor.execute("SELECT title, author, media, description FROM media WHERE title = ?", ('Blow',),).fetchall()
print(rows)



print("Total Changes:  ")
print(connection.total_changes)

