from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Конфиг сервиса нотификации"""

    pg_host: str = Field('localhost', env='POSTGRES_HOST')
    pg_port: int = Field('5432', env='POSTGRES_PORT')
    pg_db: str = Field(..., env='POSTGRES_DB')
    pg_user: str = Field(..., env='POSTGRES_USER')
    pg_password: str = Field(..., env='POSTGRES_PASSWORD')

    mail_server_host: str = Field('localhost', env='MAIL_SERVER_HOST')
    mail_server_port: int = Field('5660', env='MAIL_SERVER_PORT')
    mail_login: str = Field(..., env='MAIL_LOGIN')
    mail_password: str = Field(..., env='MAIL_PASSWD')

    test_email: str = Field(..., env='TEST_EMAIL')
    test_template: str = Field(..., env='TEST_TEMPLATE')

    queue_name_mailing: str = Field(..., env='QUEUE_NAME_MAILING')  # email.send-mailing

    class Config:
        env_file = "core/.env"
        env_file_encoding = "utf-8"


settings = Settings()
