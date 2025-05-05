import sqlite3

conn = sqlite3.connect("travel_data.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM twitter_data")
rows = cursor.fetchall()

for row in rows:
    print(f"\n🆔 ID: {row[0]}")
    print(f"📝 Text: {row[1]}")
    print(f"🕒 Date: {row[2]}")

conn.close()
