import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

DATABASE = './src/database/movies.db'
'''
# SQL -----------------------------------------------------------------------------------
def index():
    with open('./src/sql/setup.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    with sqlite3.connect('./src/database/movies.db') as connection:
        cursor = connection.cursor()
        cursor.executescript(sql_script)
        cursor.execute("SELECT * FROM Movies WHERE YEAR >= 1961 AND YEAR <= 1970;")
        print(cursor.fetchall())
#----------------------------------------------------------------------------------------
'''

def init_db():
    with open('./src/sql/setup.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    with sqlite3.connect('./src/database/movies.db') as connection:
        cursor = connection.cursor()
        cursor.executescript(sql_script)

# Show the initial page
@app.route('/')
def main():
    return render_template('catalogue.html')

# Handle dropdown menu requests from html
@app.route('/', methods = ['POST'])
def catalogue():
    pass # WORK FROM HERE. Need to link dropdown menu requests to sqlite3


if __name__ == '__main__':
    app.run()