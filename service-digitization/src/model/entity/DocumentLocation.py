"""
    @description - Entidad ubicacion del documento
    @version - 1.0.0
    @creation-date - 2022-06-13
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from pydantic import BaseModel

class DocumentLocation(BaseModel):
    id:str
    name: str
    id_box: str
    date:str