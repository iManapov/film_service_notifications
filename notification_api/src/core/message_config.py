from pydantic import BaseSettings


class LikeEvent(BaseSettings):
    subject: str = 'Вам поставили лайк!'
    routing_key: str = 'user-reporting.v1.like'


class NewContentEvent(BaseSettings):
    subject: str = 'Новая серия!'
    routing_key: str = 'user-reporting.v1.new-content'


class PaymentEvent(BaseSettings):
    subject: str = 'Успешный платеж'
    routing_key: str = 'user-reporting.v1.payment'


class WelcomeEvent(BaseSettings):
    subject: str = 'Добро пожаловать'
    routing_key: str = 'user-reporting.v1.registered'


class Mailing(BaseSettings):
    routing_key: str = 'user-reporting.v1.mailing'


class Messages(BaseSettings):
    """Конфиг сервиса уведомлений"""

    like = LikeEvent()
    new_content = NewContentEvent()
    payment = PaymentEvent()
    welcome = WelcomeEvent()
    mailing = Mailing()


messages = Messages()
