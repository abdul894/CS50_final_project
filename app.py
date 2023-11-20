import os
import sqlite3

from flask import Flask, flash, redirect, render_template, request, session, g, current_app
from flask_session import Session

app = Flask(__name__)
app.config["DATABASE"] = 'sqlite:///fumo.db'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

print("Database Path:", app.config["DATABASE"])

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            'sqlite:///fumo.db',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

@app.before_request
def init_db():
    db = get_db()

    with current_app.open_resource('db.sql') as f:
        db.executescript(f.read().decode('utf8'))


@app.route("/")
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)