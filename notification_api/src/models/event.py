import uuid

from src.models.json_mixin import JsonMixin


class EventRequestBody(JsonMixin):
    """Base model for event notifications"""

    user_id: uuid.UUID


class RegistrationEvent(EventRequestBody):
    """Model for registration event"""


class PaymentEvent(EventRequestBody):
    """Model for payment event"""

    amount: float
    service: str


class LikeEvent(EventRequestBody):
    """Model for new like event"""

    comment_id: uuid.UUID
    like_count: int


class NewContentEvent(EventRequestBody):
    """Model for new content event"""

    content_id: uuid.UUID
