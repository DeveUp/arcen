from pydantic import BaseModel
from datetime import datetime


class ShelfResponse(BaseModel):
    id: int
    id_dependence: int
    id_type_shelf: int
    id_furniture: int
    number_shelf: int
    date: datetime

    class Config:
        orm_mode = True