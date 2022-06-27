"""
    @name - FindByLetterAndFlatBlockService
    @description - Servicio para consultar un bloque por su letra y piso
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.service.IService import IService

from src.persistence.repository.block.FindByLetterAndFlatBlockRepository import FindByLetterAndFlatBlockRepository
from src.persistence.schema.BlockSchema import BlockSchema

from src.util.constant import RESPONSE
from src.util.common import get_exception_http

class FindByLetterAndFlatBlockService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindByLetterAndFlatBlockRepository(db)
        self.schema = BlockSchema()

    # @override
    # @method - Consulta un bloque por su letra y piso
    # @parameter - data - Json con letra y piso del bloque
    # @return - Block
    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element= None
        finally:
            if element == None:
                raise get_exception_http(RESPONSE['block']['get']['find_by_letter_and_flat']['error']['default'])
        return element