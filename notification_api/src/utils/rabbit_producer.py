from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.utils.async_rabbit import AsyncRabbit


class AbstractProducer(ABC):
    """Абстрактный класс для подключения к хранилищу."""

    @abstractmethod
    def send(self, message: str, routing_key: str):
        """Метод отправки данных в хранилище"""
        pass


@dataclass
class RabbitProducer(AbstractProducer):
    """
    Класс для отправки данных в Kafka
    """
    rabbit: AsyncRabbit

    async def send(self, message: str, routing_key: str):
        """
        Метод отправки данных в Rabbit.

        :param message: Сообщение
        :param routing_key: Ключ маршрутизации
        """

        await self.rabbit.send(message=message, routing_key=routing_key)

