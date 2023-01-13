from typing import Optional

from asyncpg.connection import Connection


postgres: Optional[Connection] = None


async def get_postgres() -> Connection:
    return postgres
