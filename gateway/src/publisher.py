#!/usr/bin/env python
import pika
import os

RABBITMQ_USER = os.environ.get("RABBITMQ_USERNAME")

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='somnoynadno.ru'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
