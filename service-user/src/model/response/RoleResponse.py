from pydantic import BaseModel
from datetime import datetime


class RoleResponse(BaseModel):
    id:int
    name: str
    date: datetime

    class Config:
        orm_mode = True