import asyncio

from fastapi import FastAPI

from app import rabbitmq
from app.endpoints.task_creation_router import task_creation_router
from app.endpoints.testing_router import testing_router

app = FastAPI(title='PumPum Math Boosting Service')


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()
    #asyncio.ensure_future(rabbitmq.consume_tasks(loop))


app.include_router(task_creation_router, prefix='/task-creation-api')
# app.include_router(testing_router, prefix='/testing-api')
