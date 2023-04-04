# A Script to Manage my Archive Database

#? Should I add the path for python3 here.

#importing sqlite3 and connecting to database

import sqlite3
connection = sqlite3.connect("mediamanager.db")
cursor = connection.cursor()

print("Welcome to Media Manager")
print("1. Insert Table")
print("2. Insert Full Values")
print("3. Update Record")
print("4. Perform Query")
print("5. Show Table")
choice = input("Choice: ")

if choice == "1"
    # To insert table
    input("Table Name: ")
    #input headers as list
    #cursor.execute("CREATE TABLE media (title TEXT, author TEXT, media TEXT, description TEXT)") 
elif
    choice == "2"
    # To add values
    title = input("title:")
    author = input("author:")
    media = input("media:")
    description = input("description:")
    print("Record:")
    print(title)
    print(author)
    print(media)
    print(description)
    okay = input("Type OK to commit")
    # To commit changes
        if okay == "OK"
        # To Insert Values
            cursor.execute("INSERT INTO media (title, author, media, description) values (?, ?, ?, ?)", 
		        (title, author, media, description))
            #commit connection:
            connection.commit()
        else
            print("Not commited")
else
    print("All done")

#To read values
#rows = cursor.execute("SELECT title, author, media, description FROM media WHERE title = ?", ('Blow',),).fetchall()
#print(rows)

# Show full table
connection.execute("SELECT * FROM media")
print(connection.fetchall)


print("Total Changes:  ")
print(connection.total_changes)
