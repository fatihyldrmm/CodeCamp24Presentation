import pika

def consume_messages(queue):
    credentials = pika.PlainCredentials(
        username="rabbitmq", password="rabbitmq")

    # kanala bağlan
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', credentials=credentials))
    channel = connection.channel()

    def callback(ch, method, properties, body):
        print(f"Received {body}")

    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
    print(f"Waiting for messages in {queue}. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    queue = input("Queue: ")
    consume_messages(queue)