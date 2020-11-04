import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(16)
    );"""
)

cursor.execute(
    """CREATE TABLE lists(
        list_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        list_title VARCHAR(32),
        active BOOLEAN
    );"""
)

cursor.execute(
    """CREATE TABLE tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        list_id INTEGER,
        task_title VARCHAR(32),
        task_desc VARCHAR(256),
        finished BOOLEAN,
        priority INTEGER,
        date_created INTEGER,
        date_due INTEGER
    );"""
)

connection.commit()
cursor.close()
connection.close()