from flask import Flask, render_template, request
import json
app = Flask(__name__)

#main index landing page
@app.route('/')
def index():
    return render_template('index.html')

#login submit route
@app.route('/login', methods = ['POST', 'GET'])
def login():
    #pulls username and password from form
    user = request.form['user']
    passwd = request.form['pass']

    #creates data dict for user and pass
    data = {}
    data['user'] = user
    data['passwd'] = passwd

    print(data)

    #creates the json object to be sent
    json_data = json.dumps(data)
    return render_template('login.html', user = user)

#registration route
@app.route('/register')
def register():
    #redirects user to registration page
    return render_template('register.html')

#new registrations route
@app.route('/new_register')
def new_register():
    #pulls user, pass, first and last names, and email from form
    user = request.form['user']
    passwd = request.form['pass']
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']

    print(data)

    #creates dictionary with pulled data
    data = {}
    data['user'] = user
    data['passwd'] = passwd
    data['fname'] = fname
    data['lname'] = lname
    data['email'] = email

    #creates json object out of dict
    json_data = json.dumps(data)
    return render_template('submit.html')