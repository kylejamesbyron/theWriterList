# A Script to Manage my Archive Database
# working

#<-- Should I add the path for python3 here.

#importing sqlite3 and connecting to database

import sqlite3
connection = sqlite3.connect("mediamanager.db")
cursor = connection.cursor()

#import linux os calls
import os

print("Welcome to Media Manager")
print("1. Insert Table")
print("2. Insert Full Values")
print("3. Update Record")
print("4. Perform Query")
print("5. Show Table")
choice = input("Choice #: ")

if choice == "1":
# To insert table
    tableName = input("Table Name: ")
    #input headers as list
    cursor.execute("CREATE TABLE media (title TEXT, author TEXT, media TEXT, description TEXT)") 

elif choice == "2":
# To add values
    title = input("title:")
    author = input("author:")
    media = input("media:")
    description = input("description:")
    os.system('clear')
    print("RECORD TO REVIEW:")
    print('Title:')
    print(title)
    print('Author:')
    print(author)
    print('Media:')
    print(media)
    print('Description:')
    print(description)
    okay = input("Type OK to commit: ")
 #  To commit changes
    if okay == "OK":
# To Insert Values
        cursor.execute("INSERT INTO media (title, author, media, description) values (?, ?, ?, ?)", 
		  (title, author, media, description))
#commit connection:
        connection.commit()
    else:
        print("Not commited")
# Updating records
elif choice == "3":
    print("Which record would you to update?: ")
#<--print("Search by with field?:  ")
    updateRecord = input("Title:  ")
    print("Which field # would you like to update?")
    print("1. Title")
    print("2. Author")
    print("3. Media")
    print("4. Description")
    updateField = input("Field:  ")

# Update Title
    if updateField == "1":
        newTitle = input("New Title: ")
        cursor.execute("UPDATE media SET title = ? WHERE title = ?", (newTitle, updateRecord))
    elif updateField == "2":
        newAuthor == input("New Author: ")
        cursor.execute("UPDATE media SET author = ? WHERE title = ?", (newAuthor, updateRecord))
    elif updateField == "3"
        newMedia = input("New Media: ")
        cursor.execute("UPDATE media SET media = ? WHERE title = ?", (newMedia, updateRecord))
    elif updateField == "4"
        newDescription = input("New Description: ")
        cursor.execute("UPDATE media SET author = ? WHERE title = ?", (newDescription, updateRecord))

 #   cursor.execute("UPDATE media SET author = ? WHERE title = ?", (newInput, updateRecord))
    connection.commit()
#<-- media currently hard coded
#<-- We should be able to search by different records other than title.
#<-- probably going to have to write submenu for each field.




#To read values
#rows = cursor.execute("SELECT title, author, media, description FROM media WHERE title = ?", ('Blow',),).fetchall()
#print(rows)

# Show full table
#cursor.execute("SELECT * FROM media")
#print(cursor.fetchall)


print("Total Changes:  ")
print(connection.total_changes)
