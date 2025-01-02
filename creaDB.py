import sqlite3


conn = sqlite3.connect('users.db')  # Crea un file SQLite chiamato 'users.db'
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL)''')
conn.commit()
conn.close()