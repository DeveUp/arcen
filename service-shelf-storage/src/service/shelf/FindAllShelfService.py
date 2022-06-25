"""
    @name - FindAllShelfService
    @description - Servicio para consultar todos los shelf
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session
from fastapi import HTTPException


from src.service.IService import IService
from src.persistence.repository.Shelf.FindAllShelfRepository import FindAllShelfRepository as FindAllRepository
from src.persistence.schema.ShelfSchema import ShelfSchema as EntitySchema

class FindAllShelfService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindAllRepository(db)
        self.schema = EntitySchema()

    # @override
    # @method - Consulta todos los shelf
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.lists(elements)
        except:
            raise HTTPException(200, "No hay estantes registrados")
        return elements        