#!/bin/bash

echo "Name:"
read name
echo "Film:"
read film
echo "Logline:"
read logline

echo "Testing sqlite"

sqlite3 data.db "INSERT INTO Screenplays Values('$name', '$film', '$logline');"

sqlite3 data.db "select * from Screenplays;
echo "Done"
