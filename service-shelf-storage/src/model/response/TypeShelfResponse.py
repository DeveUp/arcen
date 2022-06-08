from pydantic import BaseModel
from datetime import datetime


class TypeShelfResponse(BaseModel):
    id: int
    number_type_shelf: int
    depth: int
    height: int
    width: int
    date: datetime

    class Config:
        orm_mode = True