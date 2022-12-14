import sqlite3


class Backend:
    def create_table(self):
        with sqlite3.connect("data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS password (
                id INTEGER PRIMARY KEY,
                website CHAR(50),
                username CHAR(25),
                password CHAR(20)
            )""")
            connection.commit()

    def create_password(self, website, username, password):
        with sqlite3.connect("data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO password VALUES(NULL, ?,?,?)""", (website, username, password))
            connection.commit()

    def view_all(self):
        with sqlite3.connect("data.db") as connection:
            cursor = connection.cursor()
            all_data = cursor.execute("SELECT * FROM password").fetchall()
            connection.commit()
            return all_data

    def view_any(self, website):
        with sqlite3.connect("data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT password FROM password WHERE website=?", (website,))
            rows = cursor.fetchall()
            connection.commit()
            for row in rows:
                return "".join(row)

    def update(self, website, username, password):
        with sqlite3.connect("data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE password SET username=?, password=? WHERE website=?", (website, username, password))
            connection.commit()

    def delete(self, website):
        with sqlite3.connect("data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM password WHERE website=?", (website,))
            connection.commit()
