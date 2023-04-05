

import sqlite3
connection = sqlite3.connect("tester.db")
cursor = connection.cursor()

# Show full table
cursor.execute("SELECT * FROM media")
print(cursor.fetchall())

import os

#randy = input("What is your name? ")

name = input(os.system("read name; echo $name"))

#os.system("read name; echo $name >> file.txt")

print("Your name: ")
print(name)
print("Total Changes:  ")
print(connection.total_changes)

