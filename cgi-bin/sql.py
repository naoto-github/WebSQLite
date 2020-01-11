#! /anaconda3/bin/python

import sqlite3

print ("Content-type:text/html\n\n")
print ("<html>")
print ("<body>")
print("<h1>SQLite on Web</h1>")

DB_FILE = "db/students.db"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

sql = "select * from students;"

for r in cursor.execute(sql):
    print("<p>" + str(r) + "</r>")

print ("</body>")
print ("</html>")    
