from abc import ABC, abstractmethod
from dataclasses import dataclass
import uuid

from asyncpg.connection import Connection


class AbstractUser(ABC):
    """Абстрактный класс для подключения к хранилищу."""

    @abstractmethod
    async def get_users_id_list(self) -> list[uuid.UUID]:
        """Метод получения всех пользователей."""
        pass


@dataclass
class PgUser(AbstractUser):
    """Класс для подключения к бд пользователей."""

    postgres: Connection

    async def get_users_id_list(self) -> list[uuid.UUID]:
        """
        Метод получения id всех пользователей.

        :return: Список id всех пользователей
        """

        result = await self.postgres.fetch('SELECT id from auth_service.users')

        return [user_id['id'] for user_id in result]


