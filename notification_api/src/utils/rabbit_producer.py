from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.utils.async_rabbit import AsyncRabbit


class AbstractProducer(ABC):
    """Abstract message producer class"""

    @abstractmethod
    def send(self, message: str, routing_key: str):
        """Send message to queue"""
        pass


@dataclass
class RabbitProducer(AbstractProducer):
    """Rabbit message producer class"""

    rabbit: AsyncRabbit

    async def send(self, message: str, routing_key: str):
        """
        Sends message to Rabbit queue

        :param message: message
        :param routing_key: routing key
        """

        await self.rabbit.send(message=message, routing_key=routing_key)

