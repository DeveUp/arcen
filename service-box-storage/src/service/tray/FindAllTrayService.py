"""
    @name - FindAllTrayService
    @description - Servicio para consultar todos los tray
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.Tray.FindAllTrayfRepository import FindAllTrayRepository as FindAllRepository
from src.persistence.schema.TraySchema import TraySchema as EntitySchema

class FindAllTrayService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindAllRepository(db)
        self.schema = EntitySchema()

    # @override
    # @method - Consulta todos los tray
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.lists(elements)
        