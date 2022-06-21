"""
    @name - TypeBoxResponse
    @description - Respuesta type Box
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from pydantic import BaseModel
from datetime import datetime


class TypeBoxResponse(BaseModel):
    id : int
    number_type_box: int
    depth: int
    height: int
    width: int
    date: datetime

    class Config:
        orm_mode = True