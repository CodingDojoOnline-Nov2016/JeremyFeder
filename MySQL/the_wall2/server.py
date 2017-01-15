from flask import Flask, session, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
from datetime import datetime
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "supermegatopsecret"
mysql = MySQLConnector(app, 'the_walldb')

name_regex = re.compile(r"^[a-zA-Z\-]+$")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    #query messages
    message_query = """SELECT messages.id,
        messages.message,
        messages.created_at,
        users.id AS user_id,
        users.first_name,
        users.last_name FROM messages
            JOIN users ON messages.users_id = users.id
            ORDER BY messages.created_at DESC"""
    messages = mysql.query_db(message_query)

    #Query comments
    comment_query = """SELECT comments.id,
        comments.comment,
        comments.created_at,
        messages.id AS message_id,
        users.id AS user_id,
        users.first_name,
        users.last_name FROM comments
            JOIN users ON comments.users_id = users.id
            JOIN messages ON comments.messages_id = messages.id
            ORDER BY comments.created_at ASC"""
    comments = mysql.query_db(comment_query)

    #check if user is logged on and pull info
    if 'user_id' not in session or not session['user_id']:
        return render_template('index.html', messages=messages, comments=comments)
    else:
        user_query = "SELECT first_name, last_name FROM users WHERE id = :id"
        user_data = { 'id': session['user_id'] }
        user = mysql.query_db(user_query, user_data)
        title = str(user[0]['first_name'])+" "+str(user[0]['last_name'])
        return render_template('index.html', user=user, messages=messages, comments=comments)

@app.route('/register') #Render Registration page
def register():
    return render_template('register.html')

@app.route('/users', methods=['POST']) #Create a new user
def create_user():
    # print request.form
    first = request.form['first-name']
    last = request.form['last-name']
    email = request.form['email']
    password = request.form['password']
    confirm = request.form['confirm']

    #Create empty error list for error handling
    errors = []

    #run form validations
    if len(first) < 1:
        errors.append('You must enter a First Name of at least 1 character!')
    elif not name_regex.match(first):
    # elif not first_name.isalpha()   <-another way to check
        errors.append('Your first name may not contain any special characters or numbers!')

    if len(last) < 1:
        errors.append('You must enter a Last Name of at least 1 character!')
    elif not name_regex.match(last):
        errors.append('Your last name may not contain any special characters or numbers!')

    if not EMAIL_REGEX.match(email):
        errors.append('Your Email Address entry is invalid')

    if len(password) < 8:
        errors.append('Your Password must contain 8 or more characters!')

    if password != confirm:
        errors.append('Your Password and Confirm Password must match!')

    if errors:
        for error in errors:
            flash(error)
            return redirect('/register')

    else:
        #First check for duplicate email adresses
        duplicate_query = "SELECT email FROM users WHERE email = :email"
        duplicate_data = { 'email': email }
        duplicate_check = mysql.query_db(duplicate_query, duplicate_data)
        if duplicate_check:
            errors.append("A user already exists with that email.  Please Sign Up with a new account or Log In!")

        else:
        # Finally Create a PW Hash!
            pw_hash = bcrypt.generate_password_hash(password)

        #Run insert query
        insert_query = """INSERT INTO users(first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"""
        insert_data = {
            'first_name': first,
            'last_name': last,
            'email': email,
            'pw_hash': pw_hash,
        }
        mysql.query_db(insert_query, insert_data)

        #query for user id
        query = "SELECT id FROM users WHERE email = :email"
        data = { 'email': email }
        user = mysql.query_db(query, data)

        #set user_id to queried id and prepare for dynamic content and login
        session['user_id'] = user[0]['id']
    return redirect('/')

@app.route('/login', methods=['POST']) #log user in
def login():
    # print request.form
    email = request.form['email']
    password = request.form['password']

    #run log in query
    query = "SELECT id, pw_hash FROM users WHERE email = :email"
    data = { 'email': email }

    try:
        user = mysql.query_db(query, data)
        #check password
        if bcrypt.check_password_hash(user[0]['pw_hash'], password):
            session['user_id'] = user[0]['id']
        else:
            flash("Incorrect User Name or Password")
    except:
        flash("No User exists with that Email Address")
    return redirect('/')

@app.route('/logout') #log user out
def logout():
    session['user_id'] = None
    return redirect('/')

@app.route('/messages', methods=['POST']) #create a new message
def create_message():
    #create error handler
    message = request.form['message']
    errors = []
    #check if user is logged in before allowing them to post into db
    if 'user_id' not in session or not session['user_id']:
        errors.append('You must be Logged In to create messages')

    #run length validation
    if len(message) < 1:
        errors.append('Message must not be empty')

    #check for errors
    if errors:
        for error in errors:
            flash(error)
        return redirect('/')
    else:
        #run insert query
        query = """INSERT INTO messages(message, created_at, updated_at, users_id) VALUES (:message, NOW(), NOW(), :users_id)"""
        data = {
            'message': message,
            'users_id': session['user_id']
        }
        mysql.query_db(query, data)
    return redirect('/')

@app.route('/comments', methods=['POST'])
def create_comment():
    messages_id = request.form['message-id']
    comment = request.form['comment']
    #create error handler
    errors = []
    #check if user is logged in before allowing to comment
    if 'user_id' not in session or not session['user_id']:
        errors.append('You must be Logged In to post a Comment')

    #run lenght validation
    if len(comment) < 1:
        errors.append('Comments cannot be blank')

    #check for errors
    if errors:
        for error in errors:
            flash(error)
        print errors
        print "*" * 75
        return redirect('/')
    else:
        #run insert query
        query = """INSERT INTO comments(comment, created_at, updated_at, users_id, messages_id) VALUES (:comment, NOW(), NOW(), :users_id, :messages_id)"""
        data = {
            'comment': comment,
            'users_id': session['user_id'],
            'messages_id': messages_id
        }
        mysql.query_db(query, data)
    return redirect('/')

@app.route('/messages/<id>/delete', methods=['POST'])
def destroy_message(id):
    message_data = { 'id': id }

    #delete corresponding comments
    comments_query = "DELETE FROM comments WHERE messages_id = :id"
    mysql.query_db(comments_query, message_data)

    #delete message
    message_query = "DELETE FROM messages WHERE id = :id"
    mysql.query_db(message_query, message_data)

    return redirect('/')

@app.route('/comments/<id>/delete', methods=['POST'])
def destroy_comment(id):
    #delete comment
    query = "DELETE FROM comments WHERE id = :id"
    data = { 'id': id }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
