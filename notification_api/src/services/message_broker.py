from fastapi import Depends

from src.db.rabbit import AsyncRabbit, get_rabbit
from src.utils.rabbit_producer import AbstractProducer, RabbitProducer
from src.models.rabbit_message import RabbitBody


class EventService:
    """Сервис взаимодействия с Rabbit."""

    def __init__(self, rabbit: AbstractProducer):
        self.rabbit = rabbit

    async def send_message(self, message: RabbitBody, routing_key: str):
        """
        Метод отправки сообщения в Rabbit

        :param message: тело сообщения
        :param routing_key: ключ маршрутизации
        """

        await self.rabbit.send(message=str(message.dict()), routing_key=routing_key)


def get_event_service(
        rabbit: AsyncRabbit = Depends(get_rabbit)
) -> EventService:
    """
    Провайдер EventService,
    с помощью Depends он сообщает, что ему необходимы AsyncRabbit
    """
    return EventService(RabbitProducer(rabbit))
