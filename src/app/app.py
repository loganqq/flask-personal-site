from flask import Flask

app = Flask(__name__)


@app.route("/")
def test():
    return "<h1>Working</h1>"
