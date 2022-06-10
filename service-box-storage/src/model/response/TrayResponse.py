from datetime import datetime
from pydantic import BaseModel

class TrayResponse(BaseModel):
    id : int
    id_shelf: int
    depth: int
    height: int
    width: int
    date: datetime

    class Config:
        orm_mode = True