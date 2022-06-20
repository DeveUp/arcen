"""
    @name - FindByIdSubObjectService
    @description - Servicio para consultar un subobjeto por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.service.IService import IService

from src.persistence.repository.subobject.FindByIdSubObjectRepository import FindByIdSubObjectRepository
from src.persistence.schema.SubObjectSchema import SubObjectSchema

from src.util.constant import RESPONSE
from src.util.common import get_exception_http

class FindByIdSubObjectService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindByIdSubObjectRepository(db)
        self.schema:SubObjectSchema = SubObjectSchema()

    # @override
    # @method - Consulta un subobjeto por su pk
    # @parameter - data - No aplica
    # @return - SubObject
    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element= None
        finally:
            if element == None:
                raise get_exception_http(RESPONSE['subobject']['get']['find_by_id']['error']['default'])
        return element