

from uuid import UUID

from fastapi import Depends

from app.models.task import Task
from app.repositories.task_creation_repository import TaskCreationRepo


class TaskCreationService():
    task_creation_repo: TaskCreationRepo

    def __init__(self, task_creation_repo: TaskCreationRepo = Depends(TaskCreationRepo)) -> None:
        self.task_creation_repo = task_creation_repo

    def get_random_task(self) -> Task:
        return self.task_creation_repo.get_random_task()

    def get_n_random_task(self, n: int) -> list[Task]:
        return self.task_creation_repo.get_n_tasks(n)

    def get_task_by_id(self, id: UUID) -> Task:
        return self.task_creation_repo.get_task_by_id(id)








