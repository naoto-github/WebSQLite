#! /anaconda3/bin/python

# ↑環境に合わせて修正が必要

import sqlite3
import cgi

print ("Content-type:text/html\n\n")
print ("<html>")
print ("<body>")
print("<h1>SQLite on Web</h1>")

# データベース・ファイル
DB_FILE = "db/students.db"

# データベースへの接続
connection = sqlite3.connect(DB_FILE)

# カーソルの取得
cursor = connection.cursor()

# フォームの取得
form = cgi.FieldStorage()

# SQL文の開始
sql = "select * from students"

# IDによる検索
if "id" in form:
    sql += " where id=\"" + form["id"].value + "\""

# SQL文の終了
sql += ";"

# SQLの実行
print("<h3>SQL: " + sql + "</h3>")
for record in cursor.execute(sql):
    print("<p>" + str(record) + "</r>")

print ("</body>")
print ("</html>")    
