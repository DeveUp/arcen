"""
    @name - FindByIdObjectService
    @description - Servicio para consultar un objeto por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.service.IService import IService

from src.persistence.repository.object.FindByIdObjectRepository import FindByIdObjectRepository
from src.persistence.schema.ObjectSchema import ObjectSchema

from src.util.constant import RESPONSE
from src.util.common import get_exception_http

class FindByIdObjectService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindByIdObjectRepository(db)
        self.schema:ObjectSchema = ObjectSchema()

    # @override
    # @method - Consulta un objeto por su pk
    # @parameter - data - Json con el pk del objeto
    # @return - Object
    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element= None
        finally:
            if element == None:
                raise get_exception_http(RESPONSE['object']['get']['find_by_id']['error']['default'])
        return element