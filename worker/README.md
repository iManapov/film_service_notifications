# Notification worker

## Local run
Firstly create env file `core/.env` with following parameters:

```dotenv
MAIL_SERVER_HOST - mail server host
MAIL_SERVER_PORT - mail server port
MAIL_LOGIN - sending email user
MAIL_PASSWD - sending email password
TEST_EMAIL - test email
TEST_TEMPLATE - test template
WELCOME_TEMPLATE - welcome template
QUEUE_NAME_MAILING - mailing queue name
QUEUE_NAME_WELCOME - welcome event queue name
POSTGRES_HOST - Postgres host
POSTGRES_PORT - Postgres port
POSTGRES_DB - Postgres database name
POSTGRES_USER - Postgres user
POSTGRES_PASSWORD - Postgres password
POSTGRES_OPTIONS - Postgres options
USERS_API_URL - auth service url
```

To run worker execute following commands:
```shell
cd src
python main_mailing.py
python main_welcome.py
```
