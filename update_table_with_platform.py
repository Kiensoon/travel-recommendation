import sqlite3

conn = sqlite3.connect("travel_data.db")
cursor = conn.cursor()

# Add 'platform' column if not exists
try:
    cursor.execute("ALTER TABLE recommendations ADD COLUMN platform TEXT")
    print("✅ 'platform' column added.")
except sqlite3.OperationalError:
    print("ℹ️ 'platform' column already exists.")

conn.commit()
conn.close()
