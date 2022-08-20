#!/usr/bin/env python
import pika, sys, os


RABBITMQ_USER = os.environ.get("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = os.environ.get("RABBITMQ_PASSWORD")
RABBITMQ_PORT = int(os.environ.get("RABBITMQ_NODE_PORT_NUMBER", "5672"))
RABBITMQ_HOST = os.environ.get("RABBITMQ_REMOTE_HOST", "localhost")

# Check env 
# print(RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_PORT, RABBITMQ_HOST)

ROUTING_KEY = 'hello'


def main():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT, '/', credentials=credentials)     
    connection = pika.BlockingConnection(parameters)
    

    channel = connection.channel()
    channel.queue_declare(queue=ROUTING_KEY)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue=ROUTING_KEY, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    
