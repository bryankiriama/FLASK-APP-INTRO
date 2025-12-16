from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Brian you are doing great Am proud of you!"


@app.route("/about")
def about():
    return "This is the About Page"


@app.route("/profile/<string:username>")
def profile(username):
    return f"Profile page of {username}"

if __name__ == "__main__":
    app.run(port=5000, debug=True)