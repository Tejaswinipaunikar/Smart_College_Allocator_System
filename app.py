from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = "your_secret_key"

DB_NAME = "college_data.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

# Hash function for passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Home route (Redirect to login if not logged in)
@app.route("/")
def home():
    if "user" in session:
        return render_template("index.html")
    return redirect(url_for("login"))

# User Registration Route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = hash_password(request.form["password"])  # Hash password

        conn = connect_db()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            conn.commit()
            conn.close()
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            return "Email already registered. Please login."

    return render_template("register.html")

# User Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = hash_password(request.form["password"])  # Hash password

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session["user"] = user[1]  # Store username in session
            return redirect(url_for("home"))
        else:
            return "Invalid email or password."

    return render_template("login.html")

# Logout Route
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# College Allocator System (Only accessible if logged in)
@app.route("/results")
def results():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("results.html")

# College Search API
@app.route('/get_colleges', methods=['POST', 'GET'])
def get_colleges():
    try:
        if request.method == 'POST':
            data = request.get_json()
            percentile = data.get('percentile')
            exam_type = data.get('exam')
        else:  # For GET requests (fallback)
            percentile = request.args.get('percentile', type=float)
            exam_type = request.args.get('exam')

        if percentile is None or exam_type is None:
            return jsonify({"error": "Missing percentile or exam type"}), 400

        conn = connect_db()
        cursor = conn.cursor()

        if exam_type == "MHT-CET":
            query = """
                SELECT colleges.name, colleges.website, colleges.annual_fees, branches.branch
                FROM branches
                JOIN colleges ON branches.college_id = colleges.id
                WHERE branches.cet_cutoff <= ?
            """
        else:
            query = """
                SELECT colleges.name, colleges.website, colleges.annual_fees, branches.branch
                FROM branches
                JOIN colleges ON branches.college_id = colleges.id
                WHERE branches.jee_cutoff <= ?
            """

        cursor.execute(query, (percentile,))
        results = cursor.fetchall()
        conn.close()

        colleges_dict = {}
        for name, website, fees, branch in results:
            if name not in colleges_dict:
                colleges_dict[name] = {
                    "name": name,
                    "website": website,
                    "fees": fees,
                    "branches": []
                }
            colleges_dict[name]["branches"].append(branch)

        return jsonify(list(colleges_dict.values()))

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)