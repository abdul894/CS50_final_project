import os
import sqlite3

from flask import Flask, flash, redirect, render_template, request, session, make_response, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
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


@app.route("/login", methods = ['GET','POST'])
def login():
    
    session.clear()

    if request.method == 'POST':
        form_data = request.form
        if not form_data['email'] or not form_data['password']:
            return make_response('Field is empty!', 403)
        db = get_db()
        user_info = db.execute(
            "SELECT * FROM users WHERE email = ?", (form_data['email'],)
        ).fetchone()

        if user_info is None:
            return make_response("User not registered!",  403)
        elif not check_password_hash(
            user_info['password'], form_data['password']
        ):
            return make_response('password mismatched', 403)
       
        session['user_id'] = user_info['id']
        session['user_type'] = user_info['type'] 
        
        if user_info['type'] == 'admin':
            return redirect('/admin')
        else:
            return redirect('/')
    else:
        return render_template('login.html')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    """Rregister user"""

    if request.method == 'POST':
        db = get_db()    
        form_data = request.form
        if not form_data['username'] or not form_data['email'] or not form_data['password']:
            return make_response('Field is empty!', 403)
        elif not form_data['con_password'] == form_data['password']:
            return make_response('Confirmed password should be same as password!')
        try:
            db.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                (form_data['username'], form_data['email'], generate_password_hash(form_data['password']))
            )
            db.commit()
        except db.IntegrityError:
            return flash('User name already registered!', 'error')
        
        userdata = db.execute(
            "SELECT id FROM users WHERE email = ?", (form_data['email'],)
        )
        user_id = userdata.fetchone()['id']

        session['user_id'] = user_id

        return redirect('/login')
    else:
        return render_template('register.html')
    
@app.route("/admin", methods = ['GET', 'POST'])
@login_required
def admin():
    return render_template('admin.html')

@app.route("/users", methods = ["GET", "POST"])
@login_required
def users():
    if request.method == 'GET':
        db = get_db()
        users_data = db.execute("SELECT * FROM users")
        return render_template("users.html", users_data=users_data)

@app.route("/delete_user", methods = ["POST"])
@login_required
def delete_user():
    db = get_db()
    user_id = request.form.get("user_id")
    if user_id:
        db.execute("DELETE FROM users WHERE id = ?", user_id)
        db.commit()
    return redirect(url_for("users"))
        
if __name__ == '__main__':
    app.run(debug=True)