import traceback
import uuid
from uuid import UUID
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.task import Task
from app.schemas.tasks import Task as DBTask


class TaskRepo:
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, Task: DBTask) -> Task:
        result = Task.from_orm(Task)
        # if task.assignee is not 0:
        #     result.assignee = self.assignee_repo.get_assignee_by_id(
        #         task.assignee)

        return result

    def _map_to_schema(self, Task: Task) -> Task:
        data = dict(Task)
        del data['id']
        data['id'] = Task.id if Task.id is not 0 else 0
        result = DBTask(**data)
        return result

    def get_tasks(self) -> list[Task]:
        Tasks = []
        # Task(id=uuid.uuid4(), title="Help me", author="fdafsf", genre="dfsdf", publisher="fdfs", description="dfsd")]

        for b in self.db.query(DBTask).all():
            Tasks.append(self._map_to_model(b))
        return Tasks

    def get_task_by_id(self, id: UUID) -> Task:
        Task = self.db \
            .query(DBTask) \
            .filter(DBTask.id == id) \
            .first()

        if Task is None:
            raise KeyError

        return Task.from_orm(Task)

    def add_task(self, Task: Task) -> Task:
        try:
            db_Task = self._map_to_schema(Task)
            self.db.add(db_Task)
            self.db.commit()
            return self._map_to_model(db_Task)
        except:
            traceback.print_exc()
            raise KeyError
