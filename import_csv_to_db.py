import sqlite3
import csv

# Connect to the SQLite database (it will create the DB file if not exists)
conn = sqlite3.connect("travel_data.db")
cursor = conn.cursor()

# Drop table if exists to reset cleanly
cursor.execute("DROP TABLE IF EXISTS recommendations")

# Create the recommendations table
cursor.execute("""
    CREATE TABLE recommendations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        platform TEXT,
        location TEXT,
        state TEXT,
        price TEXT,
        rating REAL,
        comment TEXT,
        type TEXT
    )
""")

# Read data from CSV and insert into table
with open("travel_recommendations.csv", newline='', encoding='utf-8') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        cursor.execute("""
            INSERT INTO recommendations (platform, location, state, price, rating, comment, type)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            row['platform'],
            row['location'],
            row['state'],
            row['price'],
            float(row['rating']),
            row['comment'],
            row['type']
        ))


# Commit changes and close connection
conn.commit()
conn.close()
print("✅ Data successfully imported to travel_data.db")

