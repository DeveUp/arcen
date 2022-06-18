"""
    @description - Entidad version del documento
    @version - 1.0.0
    @creation-date - 2022-06-13
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from pydantic import BaseModel

class DocumentVersion(BaseModel):
    id:str
    id_document_location: str
    version: str
    date:str