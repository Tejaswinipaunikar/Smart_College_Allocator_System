import sqlite3

DB_NAME = "college_data.db"

# Connect to the database (DOES NOT DELETE existing data)
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Add users table ONLY if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
""")

conn.commit()
conn.close()
print("✅ Users table added (if it didn't exist).")
