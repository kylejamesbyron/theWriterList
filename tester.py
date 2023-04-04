

import sqlite3
connection = sqlite3.connect("tester.db")
cursor = connection.cursor()

# Show full table
cursor.execute("SELECT * FROM media")
print(cursor.fetchall())


print("Total Changes:  ")
print(connection.total_changes)
