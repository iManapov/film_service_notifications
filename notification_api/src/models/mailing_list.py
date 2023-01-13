import uuid

from src.models.json_mixin import JsonMixin


class MailingBody(JsonMixin):
    """Модель тела запроса для массовой рассылки."""

    subject: str
    template_id: uuid.UUID
    context: dict
