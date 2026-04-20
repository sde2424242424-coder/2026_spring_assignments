import sqlite3

def init_db():
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id TEXT,
        gender TEXT,
        payment TEXT,
        city TEXT,
        grade TEXT,
        satisfaction INTEGER,
        last_login INTEGER,
        temperature REAL,
        age INTEGER,
        quantity INTEGER,
        total INTEGER
    )
    """)

    conn.commit()
    return conn