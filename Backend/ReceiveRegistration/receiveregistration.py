#!/usr/bin/env python
import pika
import time
import json
import mysql.connector



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

    add_user = """INSERT INTO USER (FIRST_NAME, LAST_NAME, USERID, PASSWORD, EMAIL, CONFIRM_PASSWORD)
               VALUES (%s , %s, 12345, %s, %s, %s) """

    records_to_insert = (regis['fname'], regis['lname'], regis['passwd'], regis['email'], 'none')

    #print('after add_user')

    cursor.execute(add_user, records_to_insert)
    print('after cursor.execute')
    cnx.commit()
    cursor.close()     
    cnx.close()       
    connection = pika.BlockingConnection(pika.ConnectionParameters('messaging'))
    channel = connection.channel()
    channel.queue_declare(queue='authReg')

    channel.basic_publish(exchange='',
                      routing_key='authReg',
                      body='registration Successful')
    print(" [x] Sent 'registration Successful'")

    connection.close()





channel.basic_consume(
    queue='registration', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()




