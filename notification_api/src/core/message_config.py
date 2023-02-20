from pydantic import BaseSettings


class LikeEvent(BaseSettings):
    subject: str = 'New like!'
    routing_key: str = 'user-reporting.v1.like'


class NewContentEvent(BaseSettings):
    subject: str = 'New content!'
    routing_key: str = 'user-reporting.v1.new-content'


class PaymentEvent(BaseSettings):
    subject: str = 'Successful payment'
    routing_key: str = 'user-reporting.v1.payment'


class WelcomeEvent(BaseSettings):
    subject: str = 'Welcome!'
    routing_key: str = 'user-reporting.v1.registered'


class Mailing(BaseSettings):
    routing_key: str = 'user-reporting.v1.mailing'


class Messages(BaseSettings):
    """Messages config"""

    like = LikeEvent()
    new_content = NewContentEvent()
    payment = PaymentEvent()
    welcome = WelcomeEvent()
    mailing = Mailing()


messages = Messages()
