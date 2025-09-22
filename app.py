from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is a vulnerable app!"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # ❌ Vulnerable SQL query (SQL Injection possible)
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
        result = cursor.fetchall()
        conn.close()

        if result:
            return "Login successful"
        else:
            return "Invalid credentials"

    # Simple login form
    return '''
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password:
