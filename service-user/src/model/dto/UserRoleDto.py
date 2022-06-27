"""
    @name - UserRoleDto
    @description - Dto user role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from pydantic import EmailStr
from pydantic import BaseModel

class UserRoleDto(BaseModel):
    id_role: int
    id_user: int
    id_dependence : int
