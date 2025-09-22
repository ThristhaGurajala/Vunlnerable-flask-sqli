# 🐍 Vulnerable Flask App — SQL Injection Demo

## 📌 Overview
This project is a deliberately vulnerable Flask web application that demonstrates how SQL Injection can bypass login authentication.  
It is built for educational and security research purposes only. ❌ Do NOT deploy this in production.

## ⚙️ Setup Instructions
Clone this repository:
git clone https://github.com/<your-username>/vulnerable-flask-app.git
cd vulnerable-flask-app

Create a virtual environment and install dependencies:
python3 -m venv venv
source venv/bin/activate
pip install flask

Create the SQLite database:
sqlite3 users.db <<EOF
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
);
INSERT INTO users (username, password) VALUES ('admin', 'admin123');
INSERT INTO users (username, password) VALUES ('test', 'test123');
EOF

Run the Flask app:
python3 app.py

Open in browser:
http://127.0.0.1:5000/

## 🔴 Vulnerability Details
The app’s login function directly injects user input into an SQL query:
cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")

This makes it vulnerable to SQL Injection.

Example attack payload:
Username:  admin' OR 1=1 --
Password: anything

This bypasses login and shows "Login Successful", even with the wrong password.

## 📊 Demo Workflow
Start the app in Kali Linux VM.  
Visit `/` → shows a welcome message.  
Visit `/login` with normal credentials:  
- admin / admin123 → works  
- test / test123 → works  
Visit `/login` with injection:  
- username: admin' OR 1=1 --  
- password: anything  
➡️ Login bypassed.

## 🔒 Disclaimer
This project is for educational purposes only.  
It shows why input validation and parameterized queries are critical.  
Do not run it on production or exposed networks.
