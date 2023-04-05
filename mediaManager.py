# A Script to Manage my Archive Database
# working

#<-- Should I add the path for python3 here.

#importing sqlite3 and connecting to database

import sqlite3
connection = sqlite3.connect("mediamanager.db")
cursor = connection.cursor()

#import linux os calls
import os


# Defining functions

def continueExit():
    entry = input("Press Enter to Continue Type EXIT to End: ")
    if entry == "":
        os.system('sleep 2s')
        os.system('clear')
    else:
        exit()

# ------------------UPDATE RECORDS FUNCTION----------------#
def updateRecords():
    #<--print("Search by with field?:  ")
    updateRecord = input("Title:  ")
    print("Which field # would you like to update?")
    print("1. Title")
    print("2. Author")
    print("3. Genre")
    print("4. Description")
    updateField = input("Field:  ")
# Update Fields
    if updateField == "1":
        newTitle = input("New Title: ")
        cursor.execute("UPDATE media SET title = ? WHERE title = ?", (newTitle, updateRecord))
    elif updateField == "2":
        newAuthor = input("New Author: ")
        cursor.execute("UPDATE media SET author = ? WHERE title = ?", (newAuthor, updateRecord))
    elif updateField == "3":
        newGenre = input("New Genre: ")
        cursor.execute("UPDATE media SET genre = ? WHERE title = ?", (newGenre, updateRecord))
    elif updateField == "4":
        newDescription = input("New Description: ")
        cursor.execute("UPDATE media SET description = ? WHERE title = ?", (newDescription, updateRecord))
    connection.commit() 



# --------->BEGIN PROGRAM Function<--------------- #    
def mediamanager():
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
        cursor.execute("CREATE TABLE media (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, genre TEXT, description TEXT)") 

    elif choice == "2":
    # To add values
        title = input("title:")
        author = input("author:")
        genre = input("genre:")
        description = input("description:")
        os.system('clear')
        print("RECORD TO REVIEW:")
        print('Title:')
        print(title)
        print('Author:')
        print(author)
        print('Genre:')
        print(genre)
        print('Description:')
        print(description)
        okay = input("Type OK to commit: ")
     #  To commit changes
        if okay == "OK":
    # To Insert Values
            cursor.execute("INSERT INTO media (title, author, genre, description) values (?, ?, ?, ?)", 
              (title, author, genre, description))
    #commit connection:
            connection.commit()
        else:
            print("Not commited")
    # Updating records
    elif choice == "3":
        print("Which record would you to update?: ")
        #updateRecord = input("Title:  ")
        updateRecords() 

    # Perform query and give option to update.
    elif choice == "4":
        print("Look for Record: ")
        print("Which field # would you like to search?")
        print("1. Title")
        print("2. Author")
        print("3. Genre")
        print("4. Description")
        searchField = input("Search Field: ")
    # search by title    
        if searchField == "1":
            searchTitle = input("Title: ")
            rows = cursor.execute("SELECT title, author, genre, description FROM media WHERE title = ?", (searchTitle,),).fetchall()
            print(rows)
            #<-- add if statement to go back to update fields.  Probably need to make 
            editAnswer = input("Would you like to edit (Y/n): ")
            if editAnswer == "Y":
                updateRecord = input("Title of Record:  ")
                updateRecords()
                #<-- here is where we execute choice 3
            else:
                print("Done")
    # search by author
        if searchField == "2":
            searchTitle = input("Author: ")
            rows = cursor.execute("SELECT title, author, genre, description FROM media WHERE author = ?", (searchTitle,),).fetchall()
            print(rows)
            #<-- add if statement to go back to update fields.  Probably need to make 
            editAnswer = input("Would you like to edit (Y/n): ")
            if editAnswer == "Y":
                updateRecords()
                #<-- here is where we execute choice 3
            else:
                print("Done")
    # search by genre
        if searchField == "3":
            searchTitle = input("Genre: ")
            rows = cursor.execute("SELECT title, author, genre, description FROM media WHERE genre = ?", (searchTitle,),).fetchall()
            print(rows)
            #<-- add if statement to go back to update fields.  Probably need to make 
            editAnswer = input("Would you like to edit (Y/n): ")
            if editAnswer == "Y":
                updateRecords()
                #<-- here is where we execute choice 3
            else:
                print("Done")
    # search by description
        if searchField == "4":
            searchTitle = input("Description: ")
            rows = cursor.execute("SELECT title, author, genre, description FROM media WHERE description = ?", (searchTitle,),).fetchall()
            print(rows)
            #<-- add if statement to go back to update fields.  Probably need to make 
            editAnswer = input("Would you like to edit (Y/n): ")
            if editAnswer == "Y":
                updateRecords()
                #<-- here is where we execute choice 3
            else:
                print("Done")
                
    #Display Records.
    elif choice == "5":
        
    # Testing formatting

    # This one works: #<-- see if I can export to csv
        os.system('clear')
        print("Your Table: ")
        selection = cursor.execute("SELECT id, title, author, genre, description FROM media")
        #for row in selection: print(row[0], ":", row[1], ":", row[2], ":", row[3]) 

        for row in selection:
            print("ID:", row[0])
            print("Title:", row[1])
            print("Author:", row[2])
            print("Genre:", row[3])
            print("Description:", row[4])
            print("")
     
    


    # Example try
    #cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    #for row in cursor:
    #   print "ID = ", row[0]
    #   print "NAME = ", row[1]
    #   print "ADDRESS = ", row[2]
    #   print "SALARY = ", row[3], "\n"



    # Not the way to print
    #    pTitle = cursor.execute("SELECT title FROM media").fetchall()
    #    pAuthor = cursor.execute("SELECT author FROM media").fetchall()
    #    pGenre = cursor.execute("SELECT genre FROM media").fetchall()
    #    pDescription = cursor.execute("SELECT description FROM media").fetchall()
    #    print(pTitle)
    #    print(pAuthor)
    #    print(pGenre)
    #    print(pDescription)
        





    # formatted_row = '{:<10} {:<6} {:>6} {:>6} {:<9} {:<9}'
    #print(formatted_row.format("Name", "Gender", "Age", "Score", "Date", "Time"))
    # for Row in Data:
     #   print(formatted_row.format(*Row))
     #   cursor.execute("SELECT title, author, genre, description FROM media").fetchall()
     #   cursor.execute("UPDATE media SET author = ? WHERE title = ?", (newInput, updateRecord))




        connection.commit()
    #<-- media currently hard coded
    #<-- We should be able to search by different records other than title.
    #<-- probably going to have to write submenu for each field.




    #To read values
    #rows = cursor.execute("SELECT title, author, genre, description FROM media WHERE title = ?", ('Blow',),).fetchall()
    #print(rows)

    # Show full table
    #cursor.execute("SELECT * FROM media")
    #print(cursor.fetchall)


    print("Total Changes:  ")
    print(connection.total_changes)
 #   os.system('sleep 2s')
 #   os.system('clear')
    continueExit()
    mediamanager()



#First call of script
mediamanager()