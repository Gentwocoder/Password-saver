import sqlite3


def create_table():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS password (
            id INTEGER PRIMARY KEY,
            website CHAR(50),
            username CHAR(25),
            password CHAR(20)
        )""")
        connection.commit()


def create_password(website, username, password):
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO password VALUES(NULL, ?,?,?)""", (website, username, password))
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
            return "".join(row)


def update(website, username, password):
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE password SET username=?, password=? WHERE website=?", (website, username, password))
        connection.commit()


def delete(website):
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM password WHERE website=?", (website,))
        connection.commit()


# print(view_all())
# create_table()
# create_password("Facebook", "1234444")
print(view_all())
