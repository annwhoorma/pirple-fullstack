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


def get_user_id(username):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()

    query1 = """
            SELECT id FROM users
            WHERE username = {username};
            """.format(username=username)
    cursor.execute(query1)
    user_id = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return user_id


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


def get_all_users():
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT username
        FROM users
        ORDER BY id DESC;
        """
    )
    db_users = cursor.fetchall()
    users = []

    users = [user[0] for user in db_users]

    connection.commit()
    cursor.close()
    connection.close()

    return users


def update_user(old_username, new_username):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    query = """
            UPDATE users
            SET username={new}
            WHERE username={old};
            """.format(new=new_username, old=old_username)
    cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()


def delete_user(username):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()

    user_id = get_user_id(username)

    query = """
            DELETE FROM users
            WHERE id = {id};

            DELETE FROM tasks
            WHERE user_id = {i};
            """.format(id=user_id, user_id=user_id)
    cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()


def create_task(username, task_title, task_desc, priority, date_created, date_due):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()

    user_id = get_user_id(username)

    cursor.execute(
        """INSERT INTO tasks(
            user_id,
            task_title,
            task_desc,
            finished,
            priority,
            date_created,
            date_due)
            VALUES(
                '{user_id}',
                '{task_title}',
                '{task_desc}',
                '{priority}',
                '{date_created}',
                '{date_due}'
            );""".format(user_id=user_id, task_title=task_title, task_desc=task_desc, 
                         priority=priority, date_created=date_created, date_due=date_due)
    )

    connection.commit()
    cursor.close()
    connection.close()


def get_all_user_tasks(username):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()

    user_id = get_user_id(username)
    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE user_id = {user_id}
        """.format(user_id=user_id)
    )
    tasks = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()

    return tasks


def update_task_title(task_id, task_title):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    query = """
            UPDATE tasks
            SET task_title={new}
            WHERE id={id};
            """.format(id=task_id, new=task_title)
    cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()

def update_task_desc(task_id, task_desc):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    query = """
            UPDATE tasks
            SET task_desc={new}
            WHERE id={id};
            """.format(id=task_id, new=task_desc)
    cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()

def update_task_priority(task_id, priority):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    query = """
            UPDATE tasks
            SET priority={new}
            WHERE id={id};
            """.format(id=task_id, new=priority)
    cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()

def update_task_due_date(task_id, date_due):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    query = """
            UPDATE tasks
            SET date_due={new}
            WHERE id={id};
            """.format(id=task_id, new=date_due)
    cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()


def delete_task(task_id):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()

    query = """
            DELETE FROM tasks
            WHERE id = {task_id};
            """.format(id=task_id)
    cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()