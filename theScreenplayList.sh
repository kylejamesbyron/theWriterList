#!/bin/bash


echo "Testing sqlite"

sqlite3 twl.db "INSERT INTO Screenplays Values('Tom', 'Johns Movie', 'A Story');"

echo "Done"
