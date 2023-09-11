from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def test():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return "<p>working</p>"
