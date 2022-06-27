"""
    @name - DependenceResponse
    @description - Respuesta dependence
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from pydantic import BaseModel

class DependenceResponse(BaseModel):
    id: int
    name: str
    code: str

    class Config:
        orm_mode = True