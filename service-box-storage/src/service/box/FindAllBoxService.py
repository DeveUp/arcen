"""
    @name - FindAllBoxService
    @description - Servicio para consultar todos los box
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.Box.FindAllBoxRepository import FindAllBoxRepository as FindAllRepository
from src.persistence.schema.BoxSchema import BoxSchema as EntitySchema

class FindAllBoxService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindAllRepository(db)
        self.schema = EntitySchema()

    # @override
    # @method - Consulta todos los box
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.lists(elements)
        