from pydantic import BaseModel
from datetime import datetime


class TypeBoxResponse(BaseModel):
    id : int
    number_type_box: int
    depth: int
    height: int
    width: int
    date: datetime

    class Config:
        orm_mode = True