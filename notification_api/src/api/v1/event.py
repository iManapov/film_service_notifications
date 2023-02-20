from fastapi import APIRouter, Depends

from src.services.message_broker import EventService, get_event_service
from src.models.event import RegistrationEvent, PaymentEvent, LikeEvent, NewContentEvent
from src.models.response import BaseResponse
from src.models.rabbit_message import RabbitBody
from src.core.message_config import messages


router = APIRouter()


@router.post('/welcome',
             response_model=BaseResponse,
             summary='Successful user registration',
             description='Endpoint for sending notification about successful user registration to Rabbit queue'
             )
async def welcome_handler(
        body: RegistrationEvent,
        event_service: EventService = Depends(get_event_service)
):
    """Sending notification about successful user registration to Rabbit queue"""

    rabbit_message = RabbitBody(subject=messages.welcome.subject, context={}, user=body.user_id)
    await event_service.send_message(message=rabbit_message, routing_key=messages.welcome.routing_key)

    return BaseResponse(msg='Notification successfully added to queue')


@router.post('/payment',
             response_model=BaseResponse,
             summary='Successful payment',
             description='Endpoint for sending notification about successful payment to Rabbit queue'
             )
async def payment_handler(
        body: PaymentEvent,
        event_service: EventService = Depends(get_event_service)
):
    """Sending notification about successful payment to Rabbit queue"""

    msg_context = {'amount': body.amount, 'service': body.service}
    rabbit_message = RabbitBody(subject=messages.payment.subject, context=msg_context, user=body.user_id)
    await event_service.send_message(message=rabbit_message, routing_key=messages.payment.routing_key)

    return BaseResponse(msg='Notification successfully added to queue')


@router.post('/like',
             response_model=BaseResponse,
             summary='Like on comment',
             description='Endpoint for sending notification about new like on comment to Rabbit queue'
             )
async def like_handler(
        body: LikeEvent,
        event_service: EventService = Depends(get_event_service)
):
    """Sending notification about new like on comment to Rabbit queue"""

    msg_context = {'comment_id': body.comment_id, 'like_count': body.like_count}

    rabbit_message = RabbitBody(subject=messages.like.subject, context=msg_context, user=body.user_id)
    await event_service.send_message(message=rabbit_message, routing_key=messages.like.routing_key)

    return BaseResponse(msg='Notification successfully added to queue')


@router.post('/newcontent',
             response_model=BaseResponse,
             summary='New content',
             description='Endpoint for sending notification about new content to Rabbit queue'
             )
async def new_content_handler(
        body: NewContentEvent,
        event_service: EventService = Depends(get_event_service)
):
    """Sending notification about new content to Rabbit queue"""

    msg_context = {'content_id': body.content_id}
    rabbit_message = RabbitBody(subject=messages.new_content.subject, context=msg_context, user=body.user_id)
    await event_service.send_message(message=rabbit_message, routing_key=messages.new_content.routing_key)

    return BaseResponse(msg='Notification successfully added to queue')
