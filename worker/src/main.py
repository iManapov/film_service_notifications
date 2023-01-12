import os
import sys
import json

import pika

from retry import retry

from utils.smtp import SMTPConnection
from core.config import settings


def on_message(channel, method_frame, header_frame, body):
    """
    Callback, вызываемый при получении сообщений в очереди
    """
    message = json.loads(str(body, 'UTF-8'))
    print(method_frame.delivery_tag)

    # при получении сообщения из очереди выполняем рассылку
    smtp_sender = SMTPConnection()
    smtp_sender.send_email(to_=settings.test_email,
                           subject=message["subject"],
                           template=settings.test_template,
                           context=message["context"])
    smtp_sender.close()

    channel.basic_ack(delivery_tag=method_frame.delivery_tag)


@retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
def consume():
    """
    Метод, прослушивающий очередь
    """
    print("Connecting...")
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.basic_consume(settings.queue_name_mailing, on_message)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        connection.close()

    except pika.exceptions.ConnectionClosedByBroker:
        print("Connection closed by broker")

    except pika.exceptions.AMQPConnectionError:
        print("Connection was closed, retrying...")


if __name__ == '__main__':
    consume()
