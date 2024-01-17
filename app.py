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

app.jinja_env.filters["rupee"] = rupee

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def home():
    db = get_db()
    product_list = db.execute("SELECT * FROM product").fetchall()
    return render_template('index.html', product_list=product_list, rupee=rupee)


@app.route("/add_to_cart", methods = ['GET', 'POST'])
@login_required
def add_to_cart():
    db = get_db()
    if request.method == "POST":
        productid = request.form.get("product_id")
        db.execute("INSERT INTO cart (userid, productid) VALUES (?, ?)", (session["user_id"], productid))
        return render_template("cart.html")
    else:
        flash("login required!")
        return redirect("/")
    
@app.route("/cart", methods = ['GET', 'POST'])
@login_required
def cart():
    db = get_db()
    productid = db.execute("SELECT productid FROM cart WHERE userid = ?", (session["user_id"],))


@app.route("/login", methods = ['GET','POST'])
def login():
    
    session.clear()

    if request.method == 'POST':
        form_data = request.form
        if not form_data['email'] or not form_data['password']:
            flash('Field is empty!')
            return render_template("login.html")
        db = get_db()
        user_info = db.execute(
            "SELECT * FROM users WHERE email = ?", (form_data['email'],)
        ).fetchone()

        if user_info is None:
            flash("User not registered!")
            return render_template("login.html")
        elif not check_password_hash(
            user_info['password'], form_data['password']
        ):
            flash("password mismatched")
            return render_template("login.html")
       
        session['user_id'] = user_info['id']
        session['user_type'] = user_info['type'] 
        
        if user_info['type'] == 'admin':
            flash("Welcome to admin dashboard! ")
            return redirect('/admin/products')
        else:
            flash("Welcome on board!")
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
            flash("Empty feild!")
            return render_template("register.html")
        elif not form_data['con_password'] == form_data['password']:
            flash('Confirmed password should be same as password!')
            return render_template("register.html")
        try:
            db.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                (form_data['username'], form_data['email'], generate_password_hash(form_data['password']))
            )
            db.commit()
        except db.IntegrityError:
            flash('User name already registered!')
            return render_template("register.html")
        
        userdata = db.execute(
            "SELECT id FROM users WHERE email = ?", (form_data['email'],)
        )
        user_id = userdata.fetchone()['id']

        session['user_id'] = user_id

        return redirect('/login')
    else:
        return render_template('register.html')
    
@app.route("/logout")
def logout():
    """Log user out"""

    session.clear()

    flash("Logout successfully!")
    return redirect("/")

@app.route("/users", methods = ["GET", "POST"])
@admin_restricted
@login_required
def users():
    if request.method == 'GET':
        db = get_db()
        users_data = db.execute("SELECT * FROM users")
        return render_template("users.html", users_data=users_data)

@app.route("/delete_user", methods = ["POST"])
@admin_restricted
@login_required
def delete_user():
    db = get_db()
    user_id = request.form.get("user_id")
    if user_id:
        db.execute("DELETE FROM users WHERE id = ?", user_id)
        db.commit()
    return redirect(url_for("users"))

@app.route("/admin/products", methods = ["GET", "POST"])
@admin_restricted
@login_required
def products():
        db = get_db()
        product_list = db.execute("SELECT * FROM product")
        return render_template("products.html", product_list=product_list, rupee=rupee)

@app.route("/delete_product", methods = ["POST"])
@admin_restricted
@login_required
def delete_product():
    db = get_db()
    product_id = request.form.get("product_id")
    if product_id:
        db.execute("DELETE FROM product WHERE id = ?", (product_id,))
        db.commit()
    return redirect(url_for("products"))

@app.route("/edit_product/<int:id>", methods = ["GET", "POST"])
@admin_restricted
@login_required
def edit_product(id):
    db = get_db()
    if request.method == "POST":
        productname = request.form['productname']
        description = request.form['description']
        category = request.form['category']
        price = request.form['price']

        if 'imageurl' in request.files:
            image_file = request.files['imageurl']
            image_url = f'{image_file.filename}'

            db.execute("UPDATE product SET name = ?, description = ?, price = ?, categoryid = ?, imageurl = ? WHERE id = ?",
            (productname, description, price, category, image_url, id))

            db.commit()   

            return redirect(url_for("products"))
    else:
        old_data = db.execute("SELECT * FROM product WHERE id = ?", (id,)).fetchone()
        category_list = db.execute("SELECT * FROM category")
        return render_template("edit_product.html", old_data=old_data, category_list=category_list)

@app.route("/add_products", methods = ["GET", "POST"])
@admin_restricted
@login_required
def add_products():
    db = get_db()
    if request.method == "POST":
        productname = request.form['productname']
        description = request.form['description']
        category = request.form['category']
        price = request.form['price']
        
        if 'imageurl' in request.files:
            image_file = request.files['imageurl']
            image_url = f'{image_file.filename}'

            db.execute("INSERT INTO product (name, description, price, imageurl, categoryid) VALUES (?, ?, ?, ?, (SELECT id FROM category WHERE id = ?))",
                        (productname, description, price, image_url, category)
            )
            db.commit()
        flash("Product added successfully!")
        return redirect(url_for('products'))
    else:
        category_list = db.execute("SELECT * FROM category")
        return render_template("add_products.html", category_list=category_list)
        
if __name__ == '__main__':
    app.run(debug=True)