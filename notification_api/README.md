# Код FAST API приложения

## Локальный запуск
Предварительно необходимо создать файл `src/core/.env` со следующими параметрами:
```dotenv
SERVICE_HOST - хост сервиса
SERVICE_PORT - порт сервиса
RABBIT_HOST - сервер RabbitMQ
RABBIT_USER - пользователь RabbitMQ
RABBIT_PSWD - пароль пользователя RabbitMQ
USERS_API_URL - http адрес api сервиса авторизации (пример http://localhost:5001/api/v1)
```

Для запуска api под `uvicorn`:
```shell
uvicorn main:app --reload --host localhost --port 8003
```
Для запуска api под `gunicorn`:
```shell
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornH11Worker --bind 0.0.0.0:8003
```

Адрес документации: http://localhost:8003/api/openapi/


## Запуск в Docker
Предварительно необходимо создать файл `src/core/docker.env` со следующими параметрами:
```dotenv
SERVICE_HOST - хост сервиса
SERVICE_PORT - порт сервиса
RABBIT_HOST - сервер RabbitMQ
RABBIT_USER - пользователь RabbitMQ
RABBIT_PSWD - пароль пользователя RabbitMQ
USERS_API_URL - http адрес api сервиса авторизации
```

Для запуска api в `Docker` необходимо выполнить команду
```shell
docker compose up --build
```

Адрес документации: http://localhost:80/api/openapi/
