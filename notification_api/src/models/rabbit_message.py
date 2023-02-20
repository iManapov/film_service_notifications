import uuid
from typing import Optional

from src.models.json_mixin import JsonMixin


class RabbitBody(JsonMixin):
    """Rabbit queue message model"""

    subject: str
    template_id: Optional[uuid.UUID]
    context: dict
    user: uuid.UUID
