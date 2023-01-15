import os
import sys
import json

import pika

from retry import retry

from utils.smtp import SMTPConnection
from core.config import settings
from core.log import logger


def on_message(channel, method_frame, header_frame, body):
    """
    Callback, вызываемый при получении сообщений в очереди
    """
    message = json.loads(str(body, 'UTF-8'))
    logger.info(f"Received message (delivery tag {method_frame.delivery_tag})")

    # при получении сообщения из очереди выполняем рассылку
    smtp_sender = SMTPConnection()
    try:
        smtp_sender.send_email(to_=settings.test_email,
                               subject=message["subject"],
                               template=settings.welcome_template,  # settings.test_template,
                               context=message["context"])
    finally:
        smtp_sender.close()

    channel.basic_ack(delivery_tag=method_frame.delivery_tag)


@retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
def consume_mail_sending(connection: pika.BlockingConnection):
    """
    Метод, прослушивающий очередь
    """
    logger.info("Connecting to RabbitMQ...")
    channel = connection.channel()
    channel.basic_consume(settings.queue_name_welcome, on_message)
    try:
        channel.start_consuming()
        logger.info("Start consuming")
    except KeyboardInterrupt:
        channel.stop_consuming()
        logger.info("Stop consuming")
        connection.close()

    except pika.exceptions.ConnectionClosedByBroker:
        logger.error("Connection closed by broker")

    except pika.exceptions.AMQPConnectionError:
        logger.error("Connection was closed, retrying...")


if __name__ == '__main__':
    connection = pika.BlockingConnection()
    consume_mail_sending(connection)
