"""
    @name - FurnitureResponse
    @description - Respuesta mueble
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from pydantic import BaseModel

class FurnitureResponse(BaseModel):
    id:int
    id_block: int
    id_type_furniture: int
    number_furniture: int
    date:str