#!/usr/bin/env python
import os
import time

import pika


RABBITMQ_USER = "user132" #os.environ.get("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = "password123" #os.environ.get("RABBITMQ_PASSWORD")

ROUTING_KEY = 'timTEst'

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
parameters = pika.ConnectionParameters('somnoynadno.ru', 5672, '/', credentials)                        
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue=ROUTING_KEY)

def publish_forever(data):
    channel.basic_publish(exchange='', routing_key=ROUTING_KEY, body=data)
    #connection.close()
