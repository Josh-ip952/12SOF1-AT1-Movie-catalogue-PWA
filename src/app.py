import sqlite3

# Define connection and cursor
connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

# Create table