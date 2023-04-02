#!/bin/bash


echo "Testing sqlite"

sqlite3 twl.db "INSERT INTO Screenplays Values('Tom', 'Johns Movie', 'A Story');"

sqlite3 twl.db "select * from Screenplays;
echo "Done"
