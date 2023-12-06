
from fastapi import FastAPI

from app.endpoints.task_creation_router import task_creation_router
from app.endpoints.testing_router import testing_router

app = FastAPI(title='PumPum Math Boosting Service')


app.include_router(task_creation_router, prefix='/task-creation-api')
app.include_router(testing_router, prefix='/testing-api')
