import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Config from .env
app.secret_key = os.getenv("SECRET_KEY", "defaultsecret")

# In-memory "users" (replace with database later)
users = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            flash("Username already exists!", "danger")
            return redirect(url_for("register"))

        # Save hashed password
        users[username] = generate_password_hash(password)
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_password_hash = users.get(username)
        if user_password_hash and check_password_hash(user_password_hash, password):
            session["user"] = username
            flash("Login successful!", "success")
            return redirect(url_for("admin"))
        else:
            flash("Invalid username or password.", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/admin")
def admin():
    if "user" not in session:
        flash("You must be logged in to access the admin page.", "warning")
        return redirect(url_for("login"))
    return render_template("admin.html", user=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
