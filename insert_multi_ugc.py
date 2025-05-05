import sqlite3

conn = sqlite3.connect("travel_data.db")
cursor = conn.cursor()

recommendations = [
    # Twitter
    ("Twitter", "Pantai Cenang", "Langkawi", "Free", 4.6, "Just visited Pantai Cenang and the view is amazing!"),
    ("Twitter", "Penang Hill", "Penang", "RM10", 4.5, "Penang Hill was super breezy and beautiful! #penangtravel"),
    # Instagram
    ("Instagram", "Batu Ferringhi", "Penang", "Free", 4.5, "Sunset at Batu Ferringhi was incredible! 🏖️"),
    ("Instagram", "KL Tower", "Kuala Lumpur", "RM49", 4.3, "KL Tower is worth the visit especially at night."),
    # RedNote
    ("RedNote", "Jonker Walk", "Melaka", "RM30", 4.7, "The food street in Jonker Walk is a must-try 😋"),
    ("RedNote", "Sky Mirror", "Selangor", "RM80", 4.4, "Sky Mirror in Kuala Selangor is magical during low tide.")
]

for r in recommendations:
    cursor.execute('''
        INSERT INTO recommendations (platform, place_name, state, price, rating, source_tweet)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', r)

conn.commit()
conn.close()

print("✅ Sample multi-platform UGC inserted.")
