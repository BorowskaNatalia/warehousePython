import sqlite3

conn = sqlite3.connect('magazyn.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS produkty (
                id INTEGER PRIMARY KEY,
                product_name TEXT NOT NULL,
                description TEXT,
                price REAL,
                quantity INTEGER
            )''')
conn.commit()
