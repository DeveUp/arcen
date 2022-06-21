"""
    @name - ShelfDto
    @description - Dto Shelf
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from unicodedata import name
from pydantic import BaseModel

class ShelfDto(BaseModel):
    id_dependence: int
    id_type_shelf: int
    id_furniture: int
    number_shelf: int