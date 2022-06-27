"""
    @name - TrayDto
    @description - Dto Tray
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from unicodedata import name
from pydantic import BaseModel

class TrayDto(BaseModel):
    id_shelf: int
    depth: int
    height: int
    width: int