from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Body

from app.services.task_creation_service import TaskCreationService
from app.models.task import Task, TaskDifficulty

task_creation_router = APIRouter(prefix='/task-creation', tags=['Task'])


@task_creation_router.get('/get-random-task')
def get_deliveries(task_creation_service: TaskCreationService = Depends(TaskCreationService)) -> Task:
    return task_creation_service.get_random_task()


@task_creation_router.post('/get-task-by-id')
def get_task_by_id(
        id: UUID,
        task_creation_service: TaskCreationService = Depends(TaskCreationService)
) -> Task:
    try:
        return task_creation_service.get_task_by_id(id=id)
    except KeyError:
        raise HTTPException(400, f'Task with id={id} doesnt exist')


@task_creation_router.get('/get-n-random-tasks')
def get_n_random_tasks(n: int, task_creation_service: TaskCreationService = Depends(TaskCreationService)) -> list[Task]:
    return task_creation_service.get_n_random_task(n=n)
