import re
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Página Inicial"

@app.route("/redirect")
def redirecting():
    return redirect(url_for("index"))


@app.route("/posts/<int:id>")
def posts(id):
    title = request.args.get("title")

    data = dict(
        path=request.path,
        content_type=request.content_type,
        referrer=request.referrer,
        method=request.method,
        title=title,
        id=id if id else 0
    )

    return data

if __name__ == "__main__":
    app.run(debug=True)