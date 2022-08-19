#!/usr/bin/env python
import os
import time

import pika


RABBITMQ_USER = os.environ.get("RABBITMQ_USERNAME", "user")
RABBITMQ_PASSWORD = os.environ.get("RABBITMQ_PASSWORD", "bitnami")
RABBITMQ_PORT = int(os.environ.get("RABBITMQ_NODE_PORT_NUMBER", 56721))
RABBITMQ_HOST = os.environ.get("RABBITMQ_NODE_HOST_NUMBER", "localhost")

# Check env 
print(RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_PORT, RABBITMQ_HOST)


ROUTING_KEY = 'hello'

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
parameters = pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT, '/', credentials)                        
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue=ROUTING_KEY)

def publish_forever():
    i = 0
    while True:
        message = 'Hello World' + str(i)
        channel.basic_publish(exchange='', routing_key=ROUTING_KEY, body=message)
        
        print(f" [x] {message}")
        i += 1
        
        time.sleep(5)
        
    connection.close()
