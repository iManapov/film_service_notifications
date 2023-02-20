from fastapi import Depends

from src.db.rabbit import AsyncRabbit, get_rabbit
from src.utils.rabbit_producer import AbstractProducer, RabbitProducer
from src.models.rabbit_message import RabbitBody


class EventService:
    """RabbitMQ service"""

    def __init__(self, rabbit: AbstractProducer):
        self.rabbit = rabbit

    async def send_message(self, message: RabbitBody, routing_key: str):
        """
        Sends message to Rabbit queue

        :param message: message body
        :param routing_key: routing key
        """

        await self.rabbit.send(message=str(message.json()), routing_key=routing_key)


def get_event_service(
        rabbit: AsyncRabbit = Depends(get_rabbit)
) -> EventService:
    """
    EventService provider
    using 'Depends', it says that it needs AsyncRabbit
    """

    return EventService(RabbitProducer(rabbit))
