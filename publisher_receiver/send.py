import pika
from dotenv import load_dotenv
import os

# Doc: https://www.rabbitmq.com/tutorials/tutorial-one-python#sending
load_dotenv()


def send_message():
    rabbitmq_url = os.getenv("RABBITMQ_URL")
    params = pika.URLParameters(rabbitmq_url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue="sanjay-queue")
    channel.basic_publish(
        exchange="", routing_key="sanjay-queue", body="User added an item to cart!"
    )
    print(" [x] Sent Message: 'User added an item to cart!'")
    connection.close()


send_message()
