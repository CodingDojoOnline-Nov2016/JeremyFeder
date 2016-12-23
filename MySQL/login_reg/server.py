# DEPENDECIES
from flask import Flask, request, redirect, render_template, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector
import re

# APP, DB, CONSTANTS
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login_reg')
name_regex = re.compile(r"^[a-zA-Z\-]+$")
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
app.secret_key = 'supertopsecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    errors = []

    if len(request.form['first_name']) < 2:
        errors.append('You must enter a First Name of at least 2 characters!')
    elif not name_regex.match(request.form['first_name']):
        errors.append('Your first name may not contain any special characters or numbers!')

    if len(request.form['last_name']) < 2:
        errors.append('You must enter a Last Name of at least 2 characters!')
    elif not name_regex.match(request.form['last_name']):
        errors.append('Your last name may not contain any special characters or numbers!')

    if not EMAIL_REGEX.match(request.form['email']):
        errors.append('Your Email Address entry is invalid')

    if len(request.form['password']) < 8:
        errors.append('Your Password must contain 8 or more characters!')

    if request.form['password'] != request.form['confirm_password']:
        errors.append('Your Confirm Password and Password must match!')

    if errors:
        for error in errors:
            flash(error)
        return redirect('/')

    else:
        flash("Success!!")
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print pw_hash

        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"

        data = {
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'password':pw_hash,
        }

        mysql.query_db(query, data)
        return redirect('/success')


@app.route('/success')
def success():
    # query = "SELECT (first_name, last_name, email) FROM users"
    # data = {
    #     'first_name':request.form['first_name'],
    #     'last_name':request.form['last_name'],
    #     'email':request.form['email'],
    # }
    # emails = mysql.query_db(query, data)
    return render_template('success.html')


app.run(debug=True)
