"""
    @name - ObjectDto
    @description - Dto objecto - Peticion
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from pydantic import BaseModel

class ObjectDto(BaseModel):
    id_type_object: int
    id_sub_object: int