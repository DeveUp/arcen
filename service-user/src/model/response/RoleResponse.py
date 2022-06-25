"""
    @name - RoleResponse
    @description - Respuesta role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from pydantic import BaseModel
from datetime import datetime


class RoleResponse(BaseModel):
    id:int
    name: str
    date: datetime

    class Config:
        orm_mode = True