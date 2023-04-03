import sqlite3

connection = sqlite3.connect("mark.db")

cursor = connection.cursor()

# To Insert Table:
#cursor.execute("CREATE TABLE media (title TEXT, author TEXT, media TEXT, description TEXT)") 

title = input("title:")
input("author:")
input("media:")
input("description:")

print(title)

# To Insert Values
cursor.execute("INSERT INTO media VALUES (title, author, media, description)")

#To read values
rows = cursor.execute("SELECT title, author, media, description FROM media WHERE title = ?", ('Linux Reality Podcast',),).fetchall()
print(rows)



print("Total Changes:  ")
print(connection.total_changes)

