# DEPENDECIES
from flask import Flask, request, redirect, render_template, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector
import re

# APP, DB, CONSTANTS
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login_reg')
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
app.secret_key = 'supertopsecret'

# SQL QUERIES
queries = {
    'create' : "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :password, NOW());",
    'index' : "SELECT * FROM users",
}

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Logic that (1) tests whether an email is valid, (2) if so, adds it to DB
        if(validateEmail(request.form['email'])):
            query = queries['create']
            data = { 'email' : request.form['email'] }
            mysql.query_db(query, data)
            flash('Successfully Registered!')
            return redirect('/success')
        else:
            # Email isn't valid, flash an error message
            flash('Not a valid email!')

    return render_template('index.html')

@app.route('/success', methods=["GET"])
def success():
    query = queries['index']
    data = {}
    emails = mysql.query_db(query, data)
    return render_template('success.html', emails=emails)


def validateEmail(email):
    # Return whether or not the email passed in is valid
    return EMAIL_REGEX.match(email)

app.run(debug=True)
