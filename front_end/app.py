from flask import Flask, render_template, request, redirect, url_for
import json
import pika
import time
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

    #creates the json object to be sent
    json_data = json.dumps(data)

    #Opening Login Send Queue
    connection = pika.BlockingConnection(pika.ConnectionParameters('messaging'))
    channel = connection.channel()
    channel.queue_declare(queue='login')

    channel.basic_publish(exchange='',
                          routing_key='',
                          body=json_data)
    print(" [x] Sent 'Login Validation Request'")
    #Closing Login Send Queue
    connection.close()

    #Opening Login Listening Queue
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='messaging'))
    channel = connection.channel()

    channel.queue_declare(queue='authLogin')


    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)   #body is the content


    channel.basic_consume(
        queue='authLogin', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    #Closing Login Listening Queue
    connection.close()

    return redirect(url_for('landing'))

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

    #Open Registration Send Queue
    connection = pika.BlockingConnection(pika.ConnectionParameters('messaging'))
    channel = connection.channel()
    channel.queue_declare(queue='registration')


    channel.basic_publish(exchange='',
                      routing_key='registration',
                      body=json_data,
                      properties=pika.BasicProperties(
                      delivery_mode = 2, # make message persistent
                      ))

    print(" [x] Sent the Json File")
    #Close Registration Close Queue
    connection.close()

    #Open Registration Listening Queue
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='messaging'))
    channel = connection.channel()

    channel.queue_declare(queue='registrationConfirmation')


    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)   #body is the content


    channel.basic_consume(
        queue='registrationConfirmation', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    #Closing Registration Listening Queue
    connection.close()

    return redirect(url_for('landing'))


@app.route('/landing')
def landing():
    return render_template('login.html')