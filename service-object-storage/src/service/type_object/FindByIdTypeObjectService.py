"""
    @name - FindByIdTypeObjectService
    @description - Servicio para consultar un tipo de objecto por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.service.IService import IService

from src.persistence.repository.type_object.FindByIdTypeObjectRepository import FindByIdTypeObjectRepository
from src.persistence.schema.TypeObjectSchema import TypeObjectSchema

from src.util.constant import RESPONSE
from src.util.common import get_exception_http

class FindByIdTypeObjectService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindByIdTypeObjectRepository(db)
        self.schema:TypeObjectSchema = TypeObjectSchema()

    # @override
    # @method - Consulta un tipo de objecto por su pk
    # @parameter - data - No aplica
    # @return - Object
    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element= None
        finally:
            if element == None:
                raise get_exception_http(RESPONSE['type_object']['get']['find_by_id']['error']['default'])
        return element