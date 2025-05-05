import sqlite3

conn = sqlite3.connect("travel_data.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS recommendations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        platform TEXT,
        place_name TEXT,
        state TEXT,
        price TEXT,
        rating REAL,
        source_tweet TEXT
    )
''')

conn.commit()
conn.close()
print("✅ recommendations table created successfully.")
