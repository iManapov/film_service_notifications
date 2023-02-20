from src.models.json_mixin import JsonMixin


class BaseResponse(JsonMixin):
    """Base response model"""

    msg: str
