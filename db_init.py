# db_init.py
import sqlite3

def create_tables():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS systems (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            status TEXT NOT NULL,
            last_maintenance DATE
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
