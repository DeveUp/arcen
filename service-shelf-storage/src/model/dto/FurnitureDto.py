"""
    @name - FurnitureDto
    @description - Dto furniture
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from pydantic import BaseModel

class FurnitureDto(BaseModel):
    id_block: int
    id_type_furniture: int
    number_furniture: int