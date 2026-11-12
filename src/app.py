import sqlite3

#----------------------------------------------------------------------------------------
with open('./src/sql/setup.sql', 'r') as sql_file:
    sql_script = sql_file.read()

with sqlite3.connect("./src/database/movies.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(sql_script)


#----------------------------------------------------------------------------------------