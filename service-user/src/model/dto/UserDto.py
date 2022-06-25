"""
    @name - UserDto
    @description - Dto user
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from pydantic import EmailStr
from pydantic import BaseModel

class UserDto(BaseModel):
    document: str
    full_name: str
    email : EmailStr
    password : str
