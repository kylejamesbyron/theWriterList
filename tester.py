

import sqlite3
connection = sqlite3.connect("tester.db")
cursor = connection.cursor()

# Show full table
cursor.execute("SELECT * FROM media")
print(cursor.fetchall())

import os

randy = input("What is your name? ")

os.system("read name; echo $name >> file.txt")


print("Total Changes:  ")
print(connection.total_changes)

