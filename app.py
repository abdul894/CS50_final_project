import os
import sqlite3

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import helpers


app = Flask(__name__)
app.config["DATABASE"] = 'db.sql'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


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