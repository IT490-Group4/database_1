import pika
import time
import json

print ("Sending the Json registration file.....")
time.sleep(60)

data = {}
data['user'] = "ddd9"
data['passwd'] = "something"
data['fname'] = "Daniel"
data['lname'] = "Drechsel"
data['email'] = "ddd9@njit.edu"

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


