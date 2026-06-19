from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    print("LOGIN ROUTE HIT")

    username = request.form.get("username")
    password = request.form.get("password")

    print("Username:", username)
    print("Password:", password)

    return """
    <h2>Form received</h2>
    <a href="/">Back</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)