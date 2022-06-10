from datetime import datetime
from pydantic import BaseModel

class BoxResponse(BaseModel):
    id : int
    id_tray: int
    id_type_box: int
    number_box : int
    date: datetime

    class Config:
        orm_mode = True