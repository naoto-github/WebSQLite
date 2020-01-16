#! /anaconda3/bin/python

import sqlite3
import cgi

print ("Content-type:text/html\n\n")
print ("<html>")
print ("<body>")
print("<h1>SQLite on Web</h1>")

DB_FILE = "db/students.db"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# SQL文
sql = "select * from students "

# CGIの処理
form = cgi.FieldStorage()

if "id" in form:
    print("<p>ID: " + form["id"].value + "</p>")
    sql += "where id=" + form["id"].value + ";"
else:
    sql += ";"

# SQLの実行
for record in cursor.execute(sql):
    print("<p>" + str(record) + "</r>")

print ("</body>")
print ("</html>")    
