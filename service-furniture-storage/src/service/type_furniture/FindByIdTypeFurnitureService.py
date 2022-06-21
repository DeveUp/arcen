"""
    @name - FindByIdTypeFurnitureService
    @description - Servicio para consultar un tipo de mueble por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.service.IService import IService

from src.persistence.repository.type_furniture.FindByIdTypeFurnitureRepository import FindByIdTypeFurnitureRepository
from src.persistence.schema.TypeFurnitureSchema import TypeFurnitureSchema

from src.util.constant import RESPONSE
from src.util.common import get_exception_http

class FindByIdTypeFurnitureService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindByIdTypeFurnitureRepository(db)
        self.schema = TypeFurnitureSchema()

    # @override
    # @method - Consulta un tipo de mueble por su pk
    # @parameter - data - Json con pk del tipo de mueble
    # @return - TypeFurniture
    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element= None
        finally:
            if element == None:
                raise get_exception_http(RESPONSE['type_furniture']['get']['find_by_id']['error']['default'])
        return element