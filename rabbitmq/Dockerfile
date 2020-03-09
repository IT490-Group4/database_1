FROM rabbitmq:3
RUN apt-get update -y
	#apt-get install -y rabbitmq-server
    #apt-get install -y python-pip python-dev
	#apt-get install -y python-pip pika
EXPOSE 5672
EXPOSE 15672

COPY . /app
WORKDIR /app
CMD rabbitmq-plugins enable rabbitmq_management


