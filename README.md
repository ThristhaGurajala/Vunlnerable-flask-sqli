# 🐍 Vulnerable Flask App — SQL Injection Demo

*Repository:* vulnerable-flask-sqli-demo  
*Description:* A deliberately vulnerable Flask web app to demonstrate SQL Injection attacks (for educational use only).  

## 📌 Overview
This project is a deliberately vulnerable Flask web application that demonstrates how SQL Injection can bypass login authentication.  
It is built for educational and security research purposes only. ❌ Do NOT deploy this in production.

## ⚙ Setup Instructions
Clone this repository:
git clone https://github.com/<your-username>/vulnerable-flask-sqli-demo.git
cd vulnerable-flask-sqli-demo

Create a virtual environment and install dependencies:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Initialize the SQLite database:
sqlite3 users.db < init_db.sql

Run the Flask app:
python3 app.py

Open in browser:
http://127.0.0.1:5000/

## 🔴 Vulnerability Details
The app’s login function directly injects user input into an SQL query:
cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")

This makes it vulnerable to SQL Injection.

### Example Attack Payload
Username:
admin' OR 1=1 --
Password:
anything

➡ This bypasses login and shows "Login successful", even with the wrong password.

## 📊 Demo Workflow
- Start the app in Kali Linux VM.  
- Visit / → shows a welcome message.  
- Visit /login with normal credentials:  
  - admin / admin123 → ✅ works  
  - test / test123 → ✅ works  
- Visit /login with injection:  
  - username: admin' OR 1=1 --  
  - password: anything  
  - Result: *Login bypassed* ✅

## 🚀 Future Improvements (How to Fix)
While this app is intentionally insecure, here’s how it should be fixed in a real-world scenario:
- ✅ Use *parameterized queries / prepared statements* instead of string concatenation.  
- ✅ Switch to *SQLAlchemy ORM* to handle database interactions safely.  
- ✅ Add *input validation & sanitization* for all user inputs.  
- ✅ Implement *secure authentication mechanisms* (hashed passwords with bcrypt/argon2).  
- ✅ Use *web application firewalls (WAFs)* to detect and block injection attempts.  

## 🔒 Disclaimer
This project is for *educational purposes only*.  
It demonstrates insecure coding practices to highlight the importance of secure development.  
Do *not* deploy this app on production systems or exposed networks.
