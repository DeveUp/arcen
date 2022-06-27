"""
    @name - UserRoleResponse
    @description - Respuesta user role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
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