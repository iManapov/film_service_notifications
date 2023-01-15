import psycopg2
from psycopg2.extensions import connection as pg_connection
from psycopg2.extras import DictCursor

from dataclasses import dataclass

from core.config import settings
from core.log import logger


class Postgres:
    connection: pg_connection

    def __init__(self):
        self.pg_settings = {
                'dbname': settings.pg_db,
                'user': settings.pg_user,
                'password': settings.pg_password,
                'host': settings.pg_host,
                'port': settings.pg_port,
                'options': settings.pg_options,
            }
        self.connection = self.get_connection()

    def get_connection(self) -> pg_connection:
        """
        Получение соединения PostgreSQL
        """
        with psycopg2.connect(**self.pg_settings, cursor_factory=DictCursor) as pg_conn:
            return pg_conn

    def execute_sql(self, query: str, parameters: tuple):
        """
        Выполняет SQL-запрос к Postgre
        """
        try:
            if self.connection.closed:
                self.connection = self.get_connection()
            cursor = self.connection.cursor()
            cursor.execute(query, parameters)
            result = cursor.fetchone()
            return result[0]

        except psycopg2.OperationalError as e:
            logger.error(f"{e}")

        finally:
            self.connection.close()
