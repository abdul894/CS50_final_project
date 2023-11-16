import os
import sqlite3

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from helpers import init_app, get_db, close_db, init_db


app = Flask(__name__)
app.config["DATABASE"] = 'sqlite:///fumo.db'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


with app.app_context():
    init_db()

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def home():
    return "Hello, World!"