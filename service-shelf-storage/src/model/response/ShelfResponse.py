"""
    @name - ShelfResponse
    @description - Respuesta shelf
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from pydantic import BaseModel
from datetime import datetime


class ShelfResponse(BaseModel):
    id: int
    id_dependence: int
    id_type_shelf: int
    id_furniture: int
    number_shelf: int
    date: datetime

    class Config:
        orm_mode = True