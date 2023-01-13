from typing import Optional

from aio_pika import Message, connect_robust
from aio_pika.abc import AbstractRobustConnection, AbstractRobustExchange, AbstractRobustChannel

from src.core.config import settings


class AsyncRabbit:
    """Класс для асинхронного подключения к Rabbit."""

    def __init__(self):
        self.__conn: Optional[AbstractRobustConnection] = None
        self.__channel: Optional[AbstractRobustChannel] = None
        self.__exchange: Optional[AbstractRobustExchange] = None
        self.__key_queue_mapping: dict = settings.rabbit_key_queue_mapping

    async def create_connection(self, connection_string: str) -> 'AsyncRabbit':
        """Метод создания подключения."""

        self.__conn = await connect_robust(connection_string)
        self.__channel = await self.__conn.channel(publisher_confirms=True)
        self.__exchange = await self.__channel.declare_exchange(
            name=settings.rabbit_exchange, type='direct', durable=True)
        for routing_key, queue_name in self.__key_queue_mapping.items():
            queue = await self.__channel.declare_queue(name=queue_name, durable=True)
            await queue.bind(exchange=self.__exchange, routing_key=routing_key)
        return self

    async def send(self, message: str, routing_key: str):
        """
        Метод отправки данных в Rabbit.

        :param message: Сообщение
        :param routing_key: Ключ маршрутизации
        """

        await self.__exchange.publish(Message(body=message.encode(), delivery_mode=2), routing_key=routing_key)

    async def close_connection(self):
        """Метод закрытие подключения."""

        await self.__conn.close()
