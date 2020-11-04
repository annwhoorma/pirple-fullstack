import sqlite3


def user_exists(username):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    query = """
            SELECT username FROM users
            WHERE username = '{username}';
            """.format(username=username)
    cursor.execute(query)
    result = cursor.fetchone()

    connection.commit()
    cursor.close()
    connection.close()

    if result == None or result[0] != username:
        return False
    return True


def auth_user(username, password):
    if not user_exists(username):
        return False

    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    query = """
            SELECT username, password FROM users
            WHERE username = '{username}';
            """.format(username=username)
    cursor.execute(query)
    result = cursor.fetchone()

    connection.commit()
    cursor.close()
    connection.close()

    if result[0] == username and result[1] == password:
        return True
    return False


def create_user(username, password):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """INSERT INTO users(
            username,
            password)
            VALUES(
                '{username}',
                '{password}'
            );""".format(username=username, password=password)
    )

    connection.commit()
    cursor.close()
    connection.close()
