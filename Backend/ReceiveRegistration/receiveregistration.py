#!/usr/bin/env python
import pika
import time
import json
import mysql.connector

regis = {}

cnx = mysql.connector.connect(user='root', password='changeme', host = 'mysql', port = 3306, database='myDB')



if cnx.is_connected():
	print("connected to sql server to receive registration data")




time.sleep(60)



connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='messaging'))
channel = connection.channel()

channel.queue_declare(queue='registration')


def callback(ch, method, properties, body):
	print(" [x] Received %r" % json.loads(body))
	regis = json.loads(body)
	cursor = cnx.cursor()
	
	add_user = """INSERT INTO USER (FIRST_NAME, LAST_NAME, USERID, PASSWORD, EMAIL, CONFIRM_PASSWORD)
    				VALUES ('cool', 'dna', 12345, 'dsads', 'this', 'none') """
    

	cursor.execute(add_user)
	cnx.commit()
	cursor.close()            
   





channel.basic_consume(
    queue='registration', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()




