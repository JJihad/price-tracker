import sqlite3

# Create a connection to the SQLite database
def create_database():
    conn = sqlite3.connect("db/price_tracker.db")
    return conn

def create_items_table(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                label TEXT,
                previous_lowest_price_date DATE NOT NULL,
                previous_lowest_price REAL
            );
        ''')
    print("Table 'items' created successfully.")