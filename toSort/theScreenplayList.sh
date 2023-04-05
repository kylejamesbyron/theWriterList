#!/bin/bash


echo "Testing sqlite"

sqlite3 twl.db "INSERT INTO Screenplays Values('Tom', 'Johns Movie', 'A Story');"

clear



sqlite3 twl.db ".mode column; select * from Screenplays;"

echo "Done"
