"""
    @name - BlockResponse
    @description - Respuesta bloque
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from pydantic import BaseModel

class BlockResponse(BaseModel):
    id: int
    letter: str
    flat: str
    id_building: int
    date: str