from flask import render_template, url_for
from bookreviews import app

@app.route("/")
def index():
    return render_template('home.html')
