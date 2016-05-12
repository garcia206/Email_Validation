from flask import Flask, redirect, request, render_template, flash, session
import re
from connect import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+-_]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')

app = Flask(__name__)
app.secret_key = 'RObBoss'
db = MySQLConnector(app, 'mydb')
print (db.query_db("select * from users;"))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
	# for readability
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    # else if email doesn't match regular expression display an "invalid email address" message
    else:
        #This should insert an email into my database??
        db.query_db("INSERT INTO users(email, created_at, updated_at) VALUES('{}', now(), now());".format(request.form['email']))
        list_of_emails = db.query_db("select email from users")
        return render_template('success.html', list_of_emails = list_of_emails)

    return redirect('/')


app.run(debug=True)
