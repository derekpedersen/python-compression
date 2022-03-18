from app import app

from flask import render_template

@app.route("/upload")
def index():
    return render_template("upload.html")