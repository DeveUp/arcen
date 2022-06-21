"""
    @name - FindAllBlockService
    @description - Servicio para consultar todos los bloques
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.service.IService import IService

from src.persistence.repository.block.FindAllBlockRepository import FindAllBlockRepository
from src.persistence.schema.BlockSchema import BlockSchema

class FindAllBlockService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.repository = FindAllBlockRepository(db)
        self.schema = BlockSchema()

    # @override
    # @method - Consulta todos los bloques
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.list(elements)
        except:
            elements = list()
        return elements