#!/usr/bin/env python
import pika
import time



connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='messaging'))
channel = connection.channel()

channel.queue_declare(queue='authReg')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='authReg', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
