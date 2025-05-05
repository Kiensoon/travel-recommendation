import sqlite3

conn = sqlite3.connect('travel_data.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    place_id INTEGER,
    name TEXT,
    comment TEXT,
    FOREIGN KEY (place_id) REFERENCES recommendations(id)
)
""")

conn.commit()
conn.close()
print("✅ Review table created.")
