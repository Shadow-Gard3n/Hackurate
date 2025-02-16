import sqlite3

Database = sqlite3.connect('users.db', check_same_thread=False)
c = Database.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (
                name TEXT,
                username TEXT UNIQUE,
                password TEXT
            )''')
Database.commit()

def add_user(name, username, password):
    c.execute("INSERT INTO users (name, username, password) VALUES (?, ?, ?)",
              (name, username, password))
    Database.commit()

def check_username_exists(username):
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    return c.fetchone()

def authenticate_user(username, password):
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return c.fetchone()  #returns none if not found

def view_users():
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    for row in rows:
        print(row)
