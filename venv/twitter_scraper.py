import tweepy
import sqlite3
import time

# Bearer Token from your Twitter Developer account
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAPyd0gEAAAAAUoloexL2GXimQUmB5luWCA2aYo8%3D9oakiqPxGlhr0lfmp7XBVlCsptsX1OsGTboZJx9IHDu35PROAw'

# Set up Tweepy Client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Connect to SQLite database
conn = sqlite3.connect("travel_data.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS twitter_data (
        id TEXT PRIMARY KEY,
        text TEXT,
        created_at TEXT,
        like_count INTEGER,
        retweet_count INTEGER
    )
''')

# List of travel-related queries
queries = [
    "#langkawi -is:retweet lang:en",
    "#penangtravel -is:retweet lang:en",
    "#cuticutimalaysia -is:retweet lang:en",
    "#visitmalaysia -is:retweet lang:en",
    "langkawi food OR hotel OR beach -is:retweet lang:en"
]

# Fetch and store tweets for each query
for query in queries:
    print(f"\n🔍 Searching: {query}")
    tweets = client.search_recent_tweets(
        query=query,
        max_results=50,
        tweet_fields=["created_at", "public_metrics"]
    )

    if tweets.data:
        for tweet in tweets.data:
            tweet_id = tweet.id
            text = tweet.text
            created_at = tweet.created_at
            like_count = tweet.public_metrics['like_count']
            retweet_count = tweet.public_metrics['retweet_count']

            # Avoid duplicate tweets (using id as primary key)
            try:
                cursor.execute('''
                    INSERT INTO twitter_data (id, text, created_at, like_count, retweet_count)
                    VALUES (?, ?, ?, ?, ?)
                ''', (tweet_id, text, created_at, like_count, retweet_count))
                print(f"✅ Saved: {tweet_id}")
            except sqlite3.IntegrityError:
                print(f"⚠️ Skipped duplicate: {tweet_id}")

    time.sleep(2)  # Delay to avoid rate limits

conn.commit()
conn.close()
print("\n✅ All queries completed and saved.")
