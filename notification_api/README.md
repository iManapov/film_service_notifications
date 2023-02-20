# Notifications Api

## Local run
Firstly create env file `src/core/.env` with following parameters:
```dotenv
SERVICE_HOST - service host
SERVICE_PORT - service port
RABBIT_HOST - RabbitMQ server
RABBIT_USER - RabbitMQ user
RABBIT_PSWD - RabbitMQ password
USERS_API_URL - http url to auth service (http://localhost:5001/api/v1)
```

To run under `uvicorn` execute following commands:
```shell
uvicorn main:app --reload --host localhost --port 8003
```

To run under `gunicorn` execute following commands:
```shell
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornH11Worker --bind 0.0.0.0:8003
```
OpenApi documentation url: http://localhost:8003/api/openapi/


## Run in Docker
Create `.env` file in the root folder of project with following parameters:
```dotenv
SERVICE_HOST - service host
SERVICE_PORT - service port
RABBIT_HOST - RabbitMQ server
RABBIT_USER - RabbitMQ user
RABBIT_PSWD - RabbitMQ password
USERS_API_URL - http url to auth service (http://localhost:5001/api/v1)
```

To run api in `Docker` execute following command:
```shell
docker compose up --build
```

OpenApi documentation url: http://localhost/api/openapi/
