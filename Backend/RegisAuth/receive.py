#!/usr/bin/env python
import pika
import time

time.sleep(60)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='messaging'))
channel = connection.channel()

channel.queue_declare(queue='authRegis')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='authRegis', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
