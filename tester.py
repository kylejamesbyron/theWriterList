

import sqlite3
connection = sqlite3.connect("tester.db")
cursor = connection.cursor()

# Show full table
connection.execute("SELECT * FROM media")
print(connection.fetchall)


print("Total Changes:  ")
print(connection.total_changes)
