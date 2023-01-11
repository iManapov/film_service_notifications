from pydantic import BaseModel
import orjson


def orjson_dumps(v, *, default):
    # orjson.dumps возвращает bytes, а pydantic требует unicode, поэтому декодируем
    return orjson.dumps(v, default=default).decode()


class JsonMixin(BaseModel):
    """Класс замены стандартной работы с json на более быструю."""
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
