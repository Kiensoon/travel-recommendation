import instaloader

# Step 1: Init and load session
L = instaloader.Instaloader()
L.load_session_from_file('kiensoon512')  # your username

# Step 2: Choose a travel account
profile = instaloader.Profile.from_username(L.context, "travelmalaysia_")

# Step 3: Get recent posts
count = 0
for post in profile.get_posts():
    print(f"\n📸 Post {count+1}:")
    print("Caption:", post.caption)
    print("Likes:", post.likes)
    print("Date:", post.date)
    print("URL: https://www.instagram.com/p/" + post.shortcode)
    count += 1
    if count == 10:
        break
