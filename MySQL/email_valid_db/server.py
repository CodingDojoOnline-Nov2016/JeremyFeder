# DEPENDECIES
from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
import re

# APP, DB, CONSTANTS
app = Flask(__name__)
mysql = MySQLConnector(app,'email_valid')
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
app.secret_key = 'blahblah'

# SQL QUERIES
queries = {
    'create' : "INSERT INTO emails (email, created_at) VALUES (:email, NOW());",
    'index' : "SELECT * FROM emails",
    'delete' : "DELETE FROM emails WHERE id = :id"
}

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Logic that (1) tests whether an email is valid, (2) if so, adds it to DB
        if(validateEmail(request.form['email'])):
            query = queries['create']
            data = { 'email' : request.form['email'] }
            mysql.query_db(query, data)
            flash('Successfully created email record!')
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

@app.route('/<id>', methods=["POST"])
def destroy(id):
    query = queries['delete']
    data = {
        'id' : id
    }
    flash('Successfully deleted email!')
    mysql.query_db(query, data)
    return redirect('/success')

def validateEmail(email):
    # Return whether or not the email passed in is valid
    return EMAIL_REGEX.match(email)

app.run(debug=True)

# @app.route('/')
# def index():
#     query = "SELECT * FROM emails"
#     emails = mysql.query_db(query)
#     return render_template("index.html", all_emails=emails)
#
# @app.route('/success', methods=['POST'])
# def create():
#     print request.form['email']
#     query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
#     data = {
#              'email': request.form['email']
#            }
#     # Run query, with dictionary values injected into the query.
#     mysql.query_db(query, data)
#     return render_template("success.html")
