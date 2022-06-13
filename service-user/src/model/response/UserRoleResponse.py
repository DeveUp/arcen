from pydantic import BaseModel
from datetime import datetime

class UserRoleResponse(BaseModel):
    id:int
    id_role: int
    id_user: int
    id_dependence : int
    status : bool
    date_creation: datetime
    date_end: datetime

    class Config:
        orm_mode = True