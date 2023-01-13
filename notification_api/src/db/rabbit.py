from typing import Optional

from src.utils.async_rabbit import AsyncRabbit


rabbit: Optional[AsyncRabbit] = None


async def get_rabbit() -> AsyncRabbit:
    return rabbit
