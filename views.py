from main import app

from flask import render_template

@app.route("/")

def index():
    return render_template("Index.html")

@app.route("/estoque")

def estoque():
    return render_template("Estoque.html")
