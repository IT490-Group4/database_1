#!/usr/bin/env python
import pika
import time
import json
import mysql.connector



time.sleep(60)



connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='messaging'))
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
    sql_select_Query = "select * from USER"
   
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
    queue='login', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()