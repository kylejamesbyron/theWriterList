import sqlite3

connection = sqlite3.connect("mark.db")

cursor = connection.cursor()

# To Insert Table:
#cursor.execute("CREATE TABLE media (title TEXT, author TEXT, media TEXT, description TEXT)") 

# To Insert Values
#cursor.execute("INSERT INTO media VALUES ('Linux Reality Podcast', 'Chess Griffin', 'Instructional', 'Apodcast for the new linux user')")

#To read values
rows = cursor.execute("SELECT title, author, media, description FROM media WHERE title = ?", ('Linux Reality Podcast',),).fetchall()
print(rows)



print("Total Changes:  ")
print(connection.total_changes)


