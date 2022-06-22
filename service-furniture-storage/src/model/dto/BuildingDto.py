"""
    @name - BuildingDto
    @description - Dto edificio
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from pydantic import BaseModel

class BuildingDto(BaseModel):
    name: str
    name_area: str
    cellar: str
    flat: str