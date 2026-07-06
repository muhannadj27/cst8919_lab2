from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

USERNAME = "admin"
PASSWORD = "password123"

@app.route("/")
def home():
    return """
    <h2>Flask Login Demo</h2>
    <form method="POST" action="/login">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    """

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        app.logger.info(f"SUCCESS LOGIN: {username}")
        return "Login Successful"

    app.logger.warning(f"FAILED LOGIN: {username}")
    return "Login Failed", 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)