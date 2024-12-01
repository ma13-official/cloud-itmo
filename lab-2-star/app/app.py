from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    db_user = open("/run/secrets/db_user").read().strip()
    db_password = open("/run/secrets/db_password").read().strip()
    return jsonify({
        "message": "Welcome to the Flask app!",
        "db_user": db_user,
        "db_password": db_password
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
