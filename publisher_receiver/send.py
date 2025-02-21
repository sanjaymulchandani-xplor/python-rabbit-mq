import pika


# Doc: https://www.rabbitmq.com/tutorials/tutorial-one-python#sending
def send_message():
    params = pika.URLParameters(
        "amqps://bfnqnkyk:0A_5b7lc8t8NhC1itQACXluDUlp6aRSR@puffin.rmq2.cloudamqp.com/bfnqnkyk"  # add your AMPQ Details URL here
    )
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue="sanjay-queue")
    channel.basic_publish(
        exchange="", routing_key="sanjay-queue", body="User added an item to cart!"
    )
    print(" [x] Sent Message: 'User added an item to cart!'")
    connection.close()


send_message()
