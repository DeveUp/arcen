"""
    @name - TypeBoxfDto
    @description - Dto Type Box
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from pydantic import BaseModel

class TypeBoxfDto(BaseModel):
    number_type_box: int
    depth: int
    height: int
    width: int