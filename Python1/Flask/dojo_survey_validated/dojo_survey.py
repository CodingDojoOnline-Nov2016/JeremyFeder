from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)

app.secret_key = "topsecret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Maximum characters allowed :(")
        return redirect('/')
    else:
        return render_template("result.html", name = request.form['name'], location = request.form['location'], language = request.form['language'], comment = request.form['comment'])
app.run(debug=True)
