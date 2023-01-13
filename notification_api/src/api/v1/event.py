from fastapi import APIRouter, Depends

from src.services.message_broker import EventService, get_event_service
from src.models.event import RegistrationEvent, PaymentEvent, LikeEvent, NewContentEvent
from src.models.response import BaseResponse
from src.models.rabbit_message import RabbitBody
from src.core.message_config import messages


router = APIRouter()


@router.post('/welcome',
             response_model=BaseResponse,
             summary='Успешная регистрация пользователя',
             description='Эндпоинт для отправка уведомления об успешной регистрации в очередь Rabbit.'
             )
async def welcome_handler(
        body: RegistrationEvent,
        event_service: EventService = Depends(get_event_service)
):
    """Отправка уведомления об успешной регистрации в очередь Rabbit."""

    rabbit_message = RabbitBody(subject=messages.welcome.subject, context={}, user=body.user_id)
    await event_service.send_message(message=rabbit_message, routing_key=messages.welcome.routing_key)

    return BaseResponse(msg='Notification successfully added to queue')


@router.post('/payment',
             response_model=BaseResponse,
             summary='Успешная оплата услуг',
             description='Эндпоинт для отправки уведомления об успешной оплате.'
             )
async def payment_handler(
        body: PaymentEvent,
        event_service: EventService = Depends(get_event_service)
):
    """Отправка уведомления об успешной оплате в очередь Rabbit."""

    msg_context = {'amount': body.amount, 'service': body.service}
    rabbit_message = RabbitBody(subject=messages.payment.subject, context=msg_context, user=body.user_id)
    await event_service.send_message(message=rabbit_message, routing_key=messages.payment.routing_key)

    return BaseResponse(msg='Notification successfully added to queue')


@router.post('/like',
             response_model=BaseResponse,
             summary='Лайк на комментарии',
             description='Эндпоинт для отправки уведомления о получении лайка на комментарий.'
             )
async def like_handler(
        body: LikeEvent,
        event_service: EventService = Depends(get_event_service)
):
    """Отправка уведомления о получении лайка на комментарий в Rabbit."""

    msg_context = {'comment_id': body.comment_id, 'like_count': body.like_count}

    rabbit_message = RabbitBody(subject=messages.like.subject, context=msg_context, user=body.user_id)
    await event_service.send_message(message=rabbit_message, routing_key=messages.like.routing_key)

    return BaseResponse(msg='Notification successfully added to queue')


@router.post('/newcontent',
             response_model=BaseResponse,
             summary='Вышла новая серия',
             description='Эндпоинт для отправки уведомления о выходе новой серии.'
             )
async def new_content_handler(
        body: NewContentEvent,
        event_service: EventService = Depends(get_event_service)
):
    """Отправка уведомления о получении лайка на комментарий в Rabbit."""

    msg_context = {'content_id': body.content_id}
    rabbit_message = RabbitBody(subject=messages.new_content.subject, context=msg_context, user=body.user_id)
    await event_service.send_message(message=rabbit_message, routing_key=messages.new_content.routing_key)

    return BaseResponse(msg='Notification successfully added to queue')
