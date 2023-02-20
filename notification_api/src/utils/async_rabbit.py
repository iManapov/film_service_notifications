from typing import Optional

from aio_pika import Message, connect_robust
from aio_pika.abc import AbstractRobustConnection, AbstractRobustExchange, AbstractRobustChannel

from src.core.config import settings


class AsyncRabbit:
    """Class for async connection to RabbitMQ"""

    def __init__(self):
        self._conn: Optional[AbstractRobustConnection] = None
        self._channel: Optional[AbstractRobustChannel] = None
        self._exchange: Optional[AbstractRobustExchange] = None
        self._key_queue_mapping: dict = settings.rabbit_key_queue_mapping

    async def create_connection(self, connection_string: str) -> 'AsyncRabbit':
        """Creates connection"""

        self._conn = await connect_robust(connection_string)
        self._channel = await self._conn.channel(publisher_confirms=True)
        self._exchange = await self._channel.declare_exchange(
            name=settings.rabbit_exchange, type='direct', durable=True)
        for routing_key, queue_name in self._key_queue_mapping.items():
            queue = await self._channel.declare_queue(name=queue_name, durable=True)
            await queue.bind(exchange=self._exchange, routing_key=routing_key)
        return self

    async def send(self, message: str, routing_key: str):
        """
        Sends message to Rabbit queue

        :param message: message
        :param routing_key: routing key
        """

        await self._exchange.publish(Message(body=message.encode(), delivery_mode=2), routing_key=routing_key)

    async def close_connection(self):
        """Closes connection"""

        await self._conn.close()
