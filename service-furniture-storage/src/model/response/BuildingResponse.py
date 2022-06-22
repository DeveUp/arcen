"""
    @name - BuildingResponse
    @description - Respuesta edificio
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from pydantic import BaseModel

class BuildingResponse(BaseModel):
    id: int
    name: str
    name_area: str
    cellar: str
    flat: str
    date: str