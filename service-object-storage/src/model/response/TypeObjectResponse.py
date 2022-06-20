"""
    @name - TypeObjectResponse
    @description - Respuesta tipo de objeto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from pydantic import BaseModel

class TypeObjectResponse(BaseModel):
    id:int
    name:str
    height:int
    width:int
    depth:int
    date:str