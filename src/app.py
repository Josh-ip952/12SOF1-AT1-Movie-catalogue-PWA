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
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Movies")
        movies = cursor.fetchall()

    return render_template('catalogue.html', movies=movies)

# Handle dropdown menu requests from html


@app.route('/', methods=['GET', 'POST'])
def catalogue():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        if request.method == 'POST':
            selected_year = request.form.get('year')
            selected_rating = request.form.get('rating')

            if selected_rating == "Best_to_worst":
                print(selected_rating)
                selected_rating = "DESC"
            elif selected_rating == "Worst_to_best":
                print(selected_rating)
                selected_rating = "ASC"
            cursor.execute(
                f"SELECT * FROM Movies ORDER BY Rating {selected_rating}")
            movies = cursor.fetchall()
            

            return render_template('catalogue.html', movies=movies)
        else:
            cursor.execute(
                "SELECT * FROM Movies")
            movies = cursor.fetchall()
            return render_template('catalogue.html', movies=movies)


if __name__ == '__main__':
    app.run(debug=True)  # !!! CHANGE BEFORE RELEASING
