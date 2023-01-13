import uuid
from typing import Optional

from src.models.json_mixin import JsonMixin


class RabbitBody(JsonMixin):
    """Модель сообщений в Rabbit."""

    subject: str
    template_id: Optional[uuid.UUID]
    context: dict
    user: uuid.UUID
