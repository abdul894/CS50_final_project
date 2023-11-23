import os
import sqlite3

from flask import Flask, flash, redirect, render_template, request, session, g, current_app, make_response
from flask_session import Session
from helpers import *


app = Flask(__name__)
app.config["DATABASE"] = 'D:\\CS50_Final_Project\\fumo.db'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
init_app(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods = ['POST'])
def login():
    if request.method == 'POST':
        if not request.form.get('username'):
            return make_response('Field is empty!', 403)


if __name__ == '__main__':
    app.run(debug=True)