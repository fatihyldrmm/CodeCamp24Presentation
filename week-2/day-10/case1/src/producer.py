import pika
import sys


if __name__ == "__main__":
    my_exchange_name = "defaultexchange"

    if len(sys.argv) > 1:
        my_exchange_name = sys.argv[1]
    else:
        print("Default exchange adı olarak 'defaultexchange' kullanılıyor.")

    credentials = pika.PlainCredentials(
        username="rabbitmq", password="rabbitmq")

    # kanala bağlan
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', credentials=credentials))
    channel = connection.channel()

    # # exchange'e bağlan
    # channel.exchange_declare(exchange=my_exchange_name, exchange_type='direct')

    # kullanıcıdan mesaj al ve ilet
    running = True
    while running:
        message = input("Mesajınızı girin (çıkmak için boş bırakın): ")

        if not message:
            running = False
            break

        routing_key = input("Routing key girin: ")

        channel.basic_publish(exchange=my_exchange_name,
                              routing_key=routing_key, body=message)
        print(f"{routing_key}@{my_exchange_name} <= gönderildi <= {message}")

    connection.close()

