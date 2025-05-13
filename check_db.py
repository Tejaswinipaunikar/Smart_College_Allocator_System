import sqlite3

conn = sqlite3.connect("college_data.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM colleges WHERE cet_cutoff <= 90")
rows = cursor.fetchall()

if rows:
    for row in rows:
        print(row)
else:
    print("No matching colleges found.")

conn.close()