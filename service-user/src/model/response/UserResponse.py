"""
    @name - UserResponse
    @description - Respuesta user
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime


class UserResponse(BaseModel):
    id:int
    document: str
    full_name: str
    email : EmailStr
    password : str
    status : bool
    session_started: bool
    date: datetime

    class Config:
        orm_mode = True