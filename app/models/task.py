# /app/models/deliveryman.py

import enum
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class TaskDifficulty(enum.Enum):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'


class Task(BaseModel):
    id: UUID
    statement: str
    difficulty: TaskDifficulty

