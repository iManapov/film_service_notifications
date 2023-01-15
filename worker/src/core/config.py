from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Конфиг сервиса нотификации"""

    pg_host: str = Field('localhost', env='POSTGRES_HOST')
    pg_port: int = Field('5432', env='POSTGRES_PORT')
    pg_db: str = Field(..., env='POSTGRES_DB')
    pg_user: str = Field(..., env='POSTGRES_USER')
    pg_password: str = Field(..., env='POSTGRES_PASSWORD')
    pg_options: str = Field(..., env='POSTGRES_OPTIONS')

    mail_server_host: str = Field('localhost', env='MAIL_SERVER_HOST')
    mail_server_port: int = Field('5660', env='MAIL_SERVER_PORT')
    mail_login: str = Field(..., env='MAIL_LOGIN')
    mail_password: str = Field(..., env='MAIL_PASSWD')

    users_api_url: str = Field(..., env='USERS_API_URL')

    test_email: str = Field(..., env='TEST_EMAIL')
    test_template: str = Field(..., env='TEST_TEMPLATE')
    welcome_template: str = Field(..., env='WELCOME_TEMPLATE')

    queue_name_mailing: str = Field(..., env='QUEUE_NAME_MAILING')  # email.send-mailing
    queue_name_welcome: str = Field(..., env='QUEUE_NAME_WELCOME')  # emails.send-welcome

    class Config:
        env_file = "core/.env"
        env_file_encoding = "utf-8"


settings = Settings()


class LoggerSettings(BaseSettings):
    """Конфиг логирования"""

    version: int = 1
    disable_existing_loggers: bool = False

    formatters: dict = {
        "default_formatter": {
            "format": '%(levelname)s\t%(asctime)s\t%(funcName)s\t"%(message)s"'
        },
    }

    handlers: dict = {
        "file_handler": {
            "class": "logging.FileHandler",
            "filename": "logs.log",
            "formatter": "default_formatter",
        },
        "stream_handler": {
            "class": "logging.StreamHandler",
            "formatter": "default_formatter",
        },
    }

    loggers: dict = {
        "my_logger": {
            "handlers": ["stream_handler"],
            "level": "DEBUG",
            "propagate": True,
        }
    }
