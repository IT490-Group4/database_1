#!/usr/bin/env python
import pika
import time
import json
import mysql.connector
import hashlib, binascii, os



time.sleep(65)



connection = pika.BlockingConnection(pika.ConnectionParameters(host='messaging'))
channel = connection.channel()
channel.queue_declare(queue='login')



def callback(ch, method, properties, body):
    print(" [x] Received %r" % json.loads(body))
    loginInfo = {}
    loginInfo = json.loads(body)
    print(loginInfo)
    cnx = mysql.connector.connect(user='root', password='changeme', host = 'mysql', port = 3306, database='myDB')
    print('after cnx')
    cursor = cnx.cursor()
    print('after cursor is made')
    sql_select_Query = "select * from REGISTRATION"
   
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ", cursor.rowcount)

    print("\nPrinting each User")
    for row in records:
        print("FIRST_NAME = ", row[0])
        print("LAST_NAME = ", row[1])
        print("USERID= ", row[2])
        print("PASSWORD  = ", row[3])
        print("EMAIL  = ", row[4])
        print("CONFIRM_PASSWORD  = ", row[5], "\n" )
        if(row[2]==loginInfo['user'] and verify_password(row[5], loginInfo['passwd'])):
            print("user Exists")
            connection1 = pika.BlockingConnection(pika.ConnectionParameters('messaging'))
            channel1 = connection1.channel()
            channel1.queue_declare(queue='authLogin')
            channel1.basic_publish(exchange='',
                            routing_key='authLogin',
                            body='Login Successful!')
            print(" [x] Sent ''Login Successful!'")


            connection1.close()




    cnx.commit()


    cursor.close()
    cnx.close()
 

#https://www.vitoshacademy.com/hashing-passwords-in-python/
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


channel.basic_consume(
    queue='login', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
