import uuid

from src.models.json_mixin import JsonMixin


class EventRequestBody(JsonMixin):
    """Базовая модель тела запроса для event уведомлений."""

    user_id: uuid.UUID


class RegistrationEvent(EventRequestBody):
    """Модель тела запроса для события регистрации пользователя."""


class PaymentEvent(EventRequestBody):
    """Модель тела запроса для события об успешной оплате услуг."""

    amount: float
    service: str


class LikeEvent(EventRequestBody):
    """Модель тела запроса для события лайка."""

    comment_id: uuid.UUID
    like_count: int


class NewContentEvent(EventRequestBody):
    """Модель тела запроса для события новый контент."""

    content_id: uuid.UUID
