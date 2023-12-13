from uuid import UUID
from pydantic import BaseModel

class Test(BaseModel):
    id: UUID
    userId: UUID
    statement: str
    answer: str
