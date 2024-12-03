import pika
import sys

def send_message():
    """Send a message to RabbitMQ."""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='test_queue')
    message = "Hello, World!"
    channel.basic_publish(exchange='', routing_key='test_queue', body=message)
    print(f" [x] Sent '{message}'")
    connection.close()

def receive_message():
    """Receive messages from RabbitMQ."""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))  # Use 'rabbitmq' as the hostname for the Docker network
    channel = connection.channel()
    channel.queue_declare(queue='test_queue')

    def callback(ch, method, properties, body):
        print(f" [x] Received '{body.decode()}'")

    channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit, press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "send":
        send_message()
    elif len(sys.argv) > 1 and sys.argv[1] == "receive":
        receive_message()
    else:
        print("Usage: python main.py [send|receive]")
