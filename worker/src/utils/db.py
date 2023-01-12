import psycopg2
from psycopg2.extensions import connection as pg_connection
from psycopg2.extras import DictCursor

from dataclasses import dataclass

from config import PostgreSettings, pg_settings
from sql import query_filmfork_ids


class Postgre:
    settings: PostgreSettings
    connection: pg_connection

    def __init__(self):
        self.settings = PostgreSettings(**pg_settings)
        self.connection = self.get_connection()

    def get_connection(self) -> pg_connection:
        """
        Получение соединения PostgreSQL
        """
        with psycopg2.connect(**pg_settings, cursor_factory=DictCursor) as pg_conn:
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
            result = cur.fetchone()
            return result[0]

        except psycopg2.OperationalError as e:
            print(f"{e}")
