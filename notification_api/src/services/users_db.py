import uuid

from fastapi import Depends
from httpx import AsyncClient

from src.db.requests import get_request
from src.core.config import settings


class UserService:
    """Сервис взаимодействия с бд пользователей."""

    def __init__(self, request: AsyncClient):
        self.request = request

    async def get_users_id_list(self) -> list[uuid.UUID]:
        """
        Получение id всех пользователей.

        :return: Список id всех пользователей
        """

        response = await self.request.get(settings.users_api_url + '/users/idlist/')

        return response.json()['result']


def get_users_service(
        request: AsyncClient = Depends(get_request)
) -> UserService:
    """
    Провайдер UserService,
    с помощью Depends он сообщает, что ему необходимы AsyncClient
    """

    return UserService(request)
