from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

name_regex = re.compile(r"^[a-zA-Z\-]+$")

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "blahblah"
mysql = MySQLConnector(app, "students")

@app.route('/')
def index():
    query = "SELECT * FROM users"
    data = mysql.query_db(query)
    return render_template('index.html', title='Student Survey', students=data)

@app.route('/students', methods=['POST'])
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



    if errors:
        for error in errors:
            flash(error)
        return redirect('/')

    else:
        flash("Good Job!")
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print pw_hash

        query = "INSERT INTO users (first_name, last_name, birth_date, password, created_at, updated_at) VALUES (:first_name, :last_name, :birth_date, :password, NOW(), NOW())"

        data = {
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'birth_date':request.form['birth_date'],
            'password':pw_hash,
        }
        
        mysql.query_db(query, data)
        return redirect('/')


app.run(debug=True)
