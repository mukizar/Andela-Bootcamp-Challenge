from flask import Flask, render_template
from data import Posts

app = Flask(__name__)

Posts = Posts()


@app.route('/')
def home():
    return render_template('home.html')


@app.route("/sign")
def login():
    return render_template("signin.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/posts")
def posts():
    return render_template("posts.html", posts= Posts)

if __name__ == '__main__':
    app.run(debug=True)