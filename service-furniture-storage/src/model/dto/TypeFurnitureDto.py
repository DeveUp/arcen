"""
    @name - TypeFurnitureDto
    @description - Dto tipo mueble
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from pydantic import BaseModel

class TypeFurnitureDto(BaseModel):
    number_type_furniture: int
    count_rack: int
    count_row: int
    depth: int
    height: int
    width: int