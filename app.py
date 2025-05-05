from flask import Flask, render_template, request, redirect 
import sqlite3

app = Flask(__name__)

# Route for the main page with filtering (search removed)
@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect("travel_data.db")
    cursor = conn.cursor()

    # Get filter values from form
    state = request.form.get("state", "")
    price_category = request.form.get("price_category", "")
    place_type = request.form.get("type", "")

    # Build query dynamically
    query = "SELECT * FROM recommendations WHERE 1=1"
    params = []

    if state:
        query += " AND state = ?"
        params.append(state)

    if price_category:
        if price_category == "LOW":
            query += " AND (price = 'Free' OR CAST(SUBSTR(price, 3) AS INTEGER) <= 50)"
        elif price_category == "MIDDLE":
            query += " AND CAST(SUBSTR(price, 3) AS INTEGER) BETWEEN 51 AND 150"
        elif price_category == "HIGH":
            query += " AND CAST(SUBSTR(price, 3) AS INTEGER) > 150"

    if place_type:
        query += " AND type = ?"
        params.append(place_type)

    cursor.execute(query, params)
    recommendations = cursor.fetchall()
    conn.close()

    return render_template("index.html", recommendations=recommendations)


# Route for deleting a review
@app.route("/delete_review/<int:review_id>", methods=["POST"])
def delete_review(review_id):
    conn = sqlite3.connect("travel_data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reviews WHERE id = ?", (review_id,))
    conn.commit()
    conn.close()
    return redirect(request.referrer)


# Route for the detail page
@app.route("/detail/<int:id>", methods=["GET", "POST"])
def detail(id):
    conn = sqlite3.connect("travel_data.db")
    cursor = conn.cursor()

    # Fetch place details
    cursor.execute("SELECT * FROM recommendations WHERE id = ?", (id,))
    place = cursor.fetchone()

    # Handle form submission
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        comment = request.form.get("comment", "").strip()

        if name and comment:
            cursor.execute(
                "INSERT INTO reviews (place_id, name, comment) VALUES (?, ?, ?)",
                (id, name, comment)
            )
            conn.commit()

    # Fetch reviews with IDs (for delete functionality)
    cursor.execute("SELECT id, name, comment FROM reviews WHERE place_id = ?", (id,))
    reviews = cursor.fetchall()

    conn.close()

    if place:
        return render_template("detail.html", place=place, reviews=reviews)
    else:
        return "Place not found", 404


if __name__ == "__main__":
    app.run(debug=True)
