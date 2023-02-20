from fastapi import APIRouter, Depends

from src.core.message_config import messages
from src.services.message_broker import EventService, get_event_service
from src.services.users_db import UserService, get_users_service
from src.models.response import BaseResponse
from src.models.rabbit_message import RabbitBody
from src.models.mailing_list import MailingBody


router = APIRouter()


@router.post('/all',
             response_model=BaseResponse,
             summary='Mailing to all users',
             description='Endpoint for sending mails for all users to Rabbit queue'
             )
async def all_handler(
        body: MailingBody,
        event_service: EventService = Depends(get_event_service),
        users_service: UserService = Depends(get_users_service)
):
    """Sending mailing to Rabbit queue"""

    users_id_list = await users_service.get_users_id_list()
    for user_id in users_id_list:
        rabbit_message = RabbitBody(**body.dict(), user=user_id)
        await event_service.send_message(message=rabbit_message, routing_key=messages.mailing.routing_key)

    return BaseResponse(msg='Notification successfully added to queue')
