from asyncio import tasks
import pika, sys, os, json
from celery import Celery
from .settings import RABBITMQ_HOST, RABBITMQ_PASSWORD, RABBITMQ_PORT, RABBITMQ_USER

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AGORA_Django.settings')

app = Celery('Handler')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
    # app.autodiscover_tasks()


# Check env 
# print(RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_PORT, RABBITMQ_HOST)

ROUTING_KEY = 'hello'


@app.task
def receiverHelloWorld():
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



def parse_data(data: bytes):
    byte_parsed = data.decode('utf8').replace("'", '"')
    json_parsed = json.loads(byte_parsed)
    return json_parsed

@app.task
def recieveJSON():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters('somnoynadno.ru', 56721, '/', credentials)     
    connection = pika.BlockingConnection(parameters)
    
    channel = connection.channel()
    channel.queue_declare(queue=ROUTING_KEY)

    def callback(ch, method, properties, body):
        try:
            parsed_data = parse_data(body)
        except Exception as e:
            print(f" \033[41m[!] Exception while parsing {body} from rabbitmq\033[0m")
            return
        print(f" [x] Received {parsed_data} type {type(parsed_data)}")

    channel.basic_consume(queue=ROUTING_KEY, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()



@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@app.task
def hello():
    return 'hello world'