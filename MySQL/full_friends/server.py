from flask import Flask, request, redirect, render_template
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
app.secret_key = 'blahblahblah'

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template("index.html", all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"
    # This creates a dictionary of data from the POST data received.
    #   Outside of this it would like like Example:
    #       first_name = request.form['first_name']
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    data = {'id': id}
    friend = mysql.query_db('SELECT * FROM friends WHERE id=:id', data)
    return render_template('edit.html', friend=friend[0])

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email WHERE id=:id"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    data = {'id': id}
    friend = mysql.query_db('DELETE FROM friends WHERE id=:id', data)
    return redirect('/')

app.run(debug=True)
