import pika
import time
import json

print ("Hello send login info sleeping...")
time.sleep(60)

loginInfo = {}
loginInfo['user'] = "ddd9"
loginInfo['passwd'] = "something"

connection = pika.BlockingConnection(pika.ConnectionParameters('messaging'))
channel = connection.channel()
channel.queue_declare(queue='login')


channel.basic_publish(exchange='',
                  routing_key='login',
                  body=json.dumps(loginInfo),
                  properties=pika.BasicProperties(
                  delivery_mode = 2, # make message persistent
                  ))


	
print(" [x] Sent the login Json File")


connection.close()