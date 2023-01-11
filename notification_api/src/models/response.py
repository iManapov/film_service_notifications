from src.models.json_mixin import JsonMixin


class BaseResponse(JsonMixin):
    """Модель ответа при записи событий."""

    msg: str
