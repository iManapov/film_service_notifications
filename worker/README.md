# Код Worker'а, выполняющего отправку сообщений

## Локальный запуск
Для запуска worker локально необходимо создать файл `core/.env` со следующими параметрами:

- MAIL_SERVER_HOST - адрес почтового сервера
- MAIL_SERVER_PORT - порт почтового сервера
- MAIL_LOGIN - имя почтового ящика с которого выполняется рассылка
- MAIL_PASSWD - пароль почтового ящика с которого выполняется рассылка
- TEST_EMAIL - имя тестового почтового ящика на который отправляются письма
- TEST_TEMPLATE - тестовый шаблон для рендеринга писем
- WELCOME_TEMPLATE - шаблон при регистрации пользователя
- QUEUE_NAME_MAILING - название очереди для массовой рассылки
- QUEUE_NAME_WELCOME - название очереди для рассылки при регистрации
- POSTGRES_HOST - хост БД Postgres
- POSTGRES_PORT - порт БД Postgres
- POSTGRES_DB - имя БД Postgres
- POSTGRES_USER - пользователь БД Postgres
- POSTGRES_PASSWORD - пароль БД Postgres
- POSTGRES_OPTIONS - опции БД Postgres

Запустить - python main_mailing.py и main_welcome.py


## Запуск в docker
Для запуска worker через docker compose необходимо создать файл `core/docker.env` с теми же параметрами
