from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Notification api config"""

    service_host: str = Field('localhost', env='SERVICE_HOST')
    service_port: int = Field(8003, env='SERVICE_PORT')

    rabbit_server: str = Field('localhost:5672', env='RABBIT_HOST')
    rabbit_user: str = Field('guest', env='RABBIT_USER')
    rabbit_pswd: str = Field('guest', env='RABBIT_PSWD')
    rabbit_exchange: str = 'notification_exchange'
    # "[сущность]-reporting.[версия].[событие]": "[микросервис].[действие-консьюмера]"
    rabbit_key_queue_mapping: dict = {
        'user-reporting.v1.payment': 'emails.send-payment-info',
        'user-reporting.v1.registered': 'emails.send-welcome',
        'user-reporting.v1.mailing': 'email.send-mailing',
        'user-reporting.v1.like': 'email.send-like',
        'user-reporting.v1.new-content': 'email.send-new-content',
    }

    users_api_url: str = Field('http://localhost:5001/api/v1', env='USERS_API_URL')

    class Config:
        env_file = "src/core/.env"
        env_file_encoding = "utf-8"


settings = Settings()
