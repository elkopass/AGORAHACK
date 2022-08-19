#!/usr/bin/env python
import os
import time

import pika


RABBITMQ_USER = os.environ.get("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = os.environ.get("RABBITMQ_PASSWORD")

ROUTING_KEY = 'hello'

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
parameters = pika.ConnectionParameters('somnoynadno.ru', 56721, '/', credentials)                        
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