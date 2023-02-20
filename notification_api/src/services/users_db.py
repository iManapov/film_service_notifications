import uuid

from fastapi import Depends
from httpx import AsyncClient

from src.db.requests import get_request
from src.core.config import settings


class UserService:
    """User service"""

    def __init__(self, request: AsyncClient):
        self.request = request

    async def get_users_id_list(self) -> list[uuid.UUID]:
        """
        Returns all users id

        :return: all users id list
        """

        response = await self.request.get(settings.users_api_url + '/users/idlist/')

        return response.json()['result']


def get_users_service(
        request: AsyncClient = Depends(get_request)
) -> UserService:
    """
    UserService provicder
    using 'Depends', it says that it needs AsyncClient
    """

    return UserService(request)
