import pika, sys, os


# Doc: https://www.rabbitmq.com/tutorials/tutorial-one-python#receiving
def main():
    rabbitmq_url = os.getenv("RABBITMQ_URL")
    params = pika.URLParameters(rabbitmq_url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue="sanjay-queue")

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(
        queue="sanjay-queue", auto_ack=True, on_message_callback=callback
    )
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
