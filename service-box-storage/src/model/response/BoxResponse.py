"""
    @name - BoxResponse
    @description - Respuesta box
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from datetime import datetime
from pydantic import BaseModel

class BoxResponse(BaseModel):
    id : int
    id_tray: int
    id_type_box: int
    number_box : int
    date: datetime

    class Config:
        orm_mode = True