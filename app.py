from flask import Flask, request, jsonify, session
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "development-secret")
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

# MongoDB connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client["user_management"]
users = db["users"]


# Registration API
@app.route("/api/register", methods=["POST"])
def register():

    data = request.get_json(silent=True) or {}

    name = data.get("name", "").strip()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not name or not email or not password:
        return jsonify({"message": "All fields are required"}), 400

    if len(password) < 8:
        return jsonify({"message": "Password must contain at least 8 characters"}), 400

    if users.find_one({"email": email}):
        return jsonify({"message": "Email already registered!"}), 409

    users.insert_one({
        "name": name,
        "email": email,
        "password": generate_password_hash(password)
    })

    return jsonify({"message": "Registration successful! Please login."}), 201


# Login API
@app.route("/api/login", methods=["POST"])
def login():

    data = request.get_json(silent=True) or {}

    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    user = users.find_one({"email": email})

    if user and check_password_hash(user["password"], password):
        session.clear()
        session["user"] = email

        return jsonify({"message": "Login successful!"}), 200

    return jsonify({"message": "Invalid email or password!"}), 401


# Current user API
@app.route("/api/me", methods=["GET"])
def current_user():

    if "user" not in session:
        return jsonify({"message": "Unauthorized"}), 401

    user = users.find_one(
        {"email": session["user"]},
        {"_id": 0, "name": 1, "email": 1}
    )

    if not user:
        session.clear()
        return jsonify({"message": "User not found"}), 404

    return jsonify({"user": user}), 200


# Logout API
@app.route("/api/logout", methods=["POST"])
def logout():

    session.clear()

    return jsonify({"message": "Logged out successfully"}), 200


# Health check
@app.route("/health", methods=["GET"])
def health():

    try:
        client.admin.command("ping")
        return jsonify({
            "status": "UP",
            "database": "Connected"
        }), 200

    except Exception:
        return jsonify({"status": "DOWN"}), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)