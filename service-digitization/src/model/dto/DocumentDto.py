"""
    @description - Dto documento
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from pydantic import BaseModel

from src.model.dto.DocumentLocationDto import DocumentLocationDto

class DocumentDto(BaseModel):
    serie: str
    subserie: str
    document: list
    path_document: str
    document_location:DocumentLocationDto
    foliation_index: str
    description: str