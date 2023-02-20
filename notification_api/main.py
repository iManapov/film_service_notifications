import sys
import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
import httpx


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.api.v1 import event, mailing
from src.core.config import settings
from src.db import rabbit, requests
from src.utils.async_rabbit import AsyncRabbit


app = FastAPI(
    title='Notifications API',
    description="Notifications API",
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    version='1.0.0'
)


@app.on_event('startup')
async def startup():
    rabbit.rabbit = AsyncRabbit()
    await rabbit.rabbit.create_connection(
        f'amqp://{settings.rabbit_user}:{settings.rabbit_pswd}@{settings.rabbit_server}/')

    requests.request = httpx.AsyncClient(verify=False)


@app.on_event("shutdown")
async def shutdown_event():
    await rabbit.rabbit.close_connection()
    await requests.request.aclose()


app.include_router(event.router, prefix='/api/v1/notifications/event', tags=['event'])
app.include_router(mailing.router, prefix='/api/v1/notifications/mailing', tags=['mailing'])


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.service_host,
        port=settings.service_port,
    )
