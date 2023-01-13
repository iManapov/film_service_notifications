import os
import smtplib

from email.message import EmailMessage
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound

from core.config import settings


class SMTPConnection:
    server: smtplib.SMTP_SSL = None

    def __init__(self):
        self.server = smtplib.SMTP_SSL(settings.mail_server_host, settings.mail_server_port)
        self.server.login(settings.mail_login, settings.mail_password)

    def connect(self):
        self.server.login(settings.mail_login, settings.mail_password)

    def send_email(self,
                   to_: str,
                   subject: str,
                   template: str,
                   context: dict):
        message = EmailMessage()
        message["From"] = settings.mail_login
        message["To"] = to_
        message["Subject"] = subject

        env = Environment(loader=FileSystemLoader(f'{os.path.dirname(__file__)}'))

        try:
            template = env.get_template(template)
        except TemplateNotFound:
            template = env.get_template(settings.test_template)

        # В метод render передаются данные, которые нужно подставить в шаблон
        output = template.render(**context)
        message.add_alternative(output, subtype='html')
        self.server.sendmail(settings.mail_login, to_, message.as_string())

    def close(self):
        self.server.close()
