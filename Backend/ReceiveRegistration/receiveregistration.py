#!/usr/bin/env python
import pika
import time
import json
import mysql.connector
import hashlib, binascii, os



time.sleep(60)



connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='messaging'))
channel = connection.channel()

channel.queue_declare(queue='registration')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % json.loads(body))
    regis = {}
    regis = json.loads(body)
    print(regis)
    cnx = mysql.connector.connect(user='root', password='changeme', host = 'mysql', port = 3306, database='myDB')
    print('after cnx')
    cursor = cnx.cursor()
    print('after cursor is made')
    stored_password = hash_password(regis['passwd'])
    print(stored_password)


    add_user = """INSERT INTO REGISTRATION (FIRST_NAME, LAST_NAME, USERNAME, PASSWORD, EMAIL, CONFIRM_PASSWORD)
               VALUES (%s , %s, %s, %s, %s, %s) """

    records_to_insert = (regis['fname'], regis['lname'], regis['user'] ,regis['passwd'], regis['email'], stored_password)

    #print('after add_user')

    cursor.execute(add_user, records_to_insert)
    print('after cursor.execute')
    cnx.commit()
    cursor.close()     
    cnx.close()       
    connection = pika.BlockingConnection(pika.ConnectionParameters('messaging'))
    channel = connection.channel()
    channel.queue_declare(queue='authRegis')

    channel.basic_publish(exchange='',
                      routing_key='authRegis',
                      body='registration Successful')
    print(" [x] Sent 'registration Successful'")

    connection.close()



def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')



channel.basic_consume(
    queue='registration', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()




