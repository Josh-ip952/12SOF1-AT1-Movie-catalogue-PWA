import sqlite3
from flask import Flask

# instance of flask application
app = Flask(__name__)

# SQL -----------------------------------------------------------------------------------
def index():
    with open('./src/sql/setup.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    with sqlite3.connect("./src/database/movies.db") as connection:
        cursor = connection.cursor()
        cursor.executescript(sql_script)
        cursor.execute("SELECT * FROM Movies WHERE YEAR >= 1961 AND YEAR <= 1970;")
        print(cursor.fetchall())
#----------------------------------------------------------------------------------------



# home route that returns below text when root url is accessed
@app.route("/")

def hello():
    return 'Hello World'

if __name__ == '__main__':  
   app.run()  
