"""
    @name - FindByIdBlockService
    @description - Servicio para consultar un mueble por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.service.IService import IService

from src.persistence.repository.furniture.FindByIdFurnitureRepository import FindByIdFurnitureRepository
from src.persistence.schema.FurnitureSchema import FurnitureSchema

from src.util.constant import RESPONSE
from src.util.common import get_exception_http

class FindByIdFurnitureService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindByIdFurnitureRepository(db)
        self.schema = FurnitureSchema()

    # @override
    # @method - Consulta un mueble por su pk
    # @parameter - data - Json con pk del mueble
    # @return - Furniture
    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element= None
        finally:
            if element == None:
                raise get_exception_http(RESPONSE['furniture']['get']['find_by_id']['error']['default'])
        return element