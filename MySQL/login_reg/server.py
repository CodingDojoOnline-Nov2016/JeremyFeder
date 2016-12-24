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

@app.route('/users/<id>/profile')
def users(id):
	query = "SELECT first_name, last_name FROM users WHERE id = :id"
	data = { 'id': id }
	user = mysql.query_db(query, data)
	return render_template('success.html', user=user)

@app.route('/users', methods=['POST'])
def create():
    errors = []

    #Check to see if user email already exists in the system
    email = request.form['email']
    email_query = "SELECT id FROM users WHERE email= :email"
    email_data = { 'email': email }
    user_check = mysql.query_db(email_query, email_data)
    if user_check:
        errors.append('A user already exists with that email in the system.  Please Login or try again.')

    if len(request.form['first_name']) < 2:
        errors.append('You must enter a First Name of at least 2 characters!')
    elif not name_regex.match(request.form['first_name']):
    # elif not first_name.isalpha()   <-another way to check
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

        #pull user_id for routing
        user_query = "SELECT id FROM users WHERE email = :email LIMIT 1"
        user_data = { 'email': email }
        user = mysql.query_db(user_query, user_data)
        flash("successful registration")
        session['user_id'] = user[0]['id']
        return redirect('/users/'+str(session['user_id'])+'/profile')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if email and password:
        user_query = "SELECT id, email, password FROM users WHERE email = :email LIMIT 1"
        query_data = { 'email': email }
        try:
            user = mysql.query_db(user_query, query_data)

            if bcrypt.check_password_hash(user[0]['password'], password):
                session['user_id'] = user[0]['id']
                flash('successful login')
                return redirect('/users/'+str(session['user_id'])+'/profile')
            else:
                flash('incorrect password')
                return redirect('/')
        except:
            flash('no user exists with that email')
            return redirect('/')
    else:
        flash('unsuccessful login')
        return redirect('/')

app.run(debug=True)
