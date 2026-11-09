import sqlite3

def init_db():

    table = """CREATE TABLE IF NOT EXISTS Movies (
  MovieID int PRIMARY KEY,
  Name varchar(255),
  Rating int
);
"""

    movies = [
        (1, "Dr. No", 95),
        (2, "From Russia with Love", 97),
        (3, "Goldfinger", 99)
    ]



    with sqlite3.connect("./src/database/movies.db") as connection:
        
        cursor = connection.cursor()
        cursor.execute(table)

        for movie in movies:
            cursor.execute("INSERT OR IGNORE INTO Movies VALUES(?, ?, ?)", movie)
        
        cursor.execute("SELECT * FROM Movies;")
        result = cursor.fetchall()
        print(result)

init_db()