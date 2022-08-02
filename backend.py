import sqlite3


def create_table():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS password (
            id INTEGER PRIMARY KEY,
            website CHAR(50),
            password CHAR(20)
        )""")
        connection.commit()


def create_password(website, password):
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO password VALUES(NULL, ?,?)""", (website, password))
        connection.commit()


def view_all():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        all_data = cursor.execute("SELECT * FROM password").fetchall()
        connection.commit()
        return all_data


def view_any(website):
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT password FROM password WHERE website=?", (website,))
        rows = cursor.fetchall()
        connection.commit()
        for row in rows:
            return row


def update(id, website, password):
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE password SET website=?, password=? WHERE id=?", (website, password, id))
        connection.commit()


def delete(id):
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM password WHERE id=?", (id,))
        connection.commit()


# create_table()
# create_password("Facebook", "1234444")
print(view_all())
