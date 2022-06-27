"""
    @name - TrayResponse
    @description - Respuesta tray
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from datetime import datetime
from pydantic import BaseModel

class TrayResponse(BaseModel):
    id : int
    id_shelf: int
    depth: int
    height: int
    width: int
    date: datetime

    class Config:
        orm_mode = True