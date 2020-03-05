import pika
import time
import json

print ("Hello sleeping sned login.....")
time.sleep(60)

data = {}
data['user'] = "haloman"
data['passwd'] = "coolCat"
data['fname'] = "coolCat"
data['lname'] = "coolCat"
data['email'] = "coolCat"

connection = pika.BlockingConnection(pika.ConnectionParameters('messaging'))
channel = connection.channel()
channel.queue_declare(queue='registration')


channel.basic_publish(exchange='',
                  routing_key='registration',
                  body=json.dumps(data),
                  properties=pika.BasicProperties(
                  delivery_mode = 2, # make message persistent
                  ))


	
print(" [x] Sent the Json File")


connection.close()


