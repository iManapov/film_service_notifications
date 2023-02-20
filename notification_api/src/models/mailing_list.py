import uuid

from src.models.json_mixin import JsonMixin


class MailingBody(JsonMixin):
    """Model for mailing"""

    subject: str
    template_id: uuid.UUID
    context: dict
