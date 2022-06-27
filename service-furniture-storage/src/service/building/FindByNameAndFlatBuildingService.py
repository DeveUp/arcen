"""
    @name - FindByNameAndFlatBuildingService
    @description - Servicio para consultar un edificio por su nombre y piso
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.service.IService import IService

from src.persistence.repository.building.FindByNameAndFlatBuildingRepository import FindByNameAndFlatBuildingRepository
from src.persistence.schema.BuildingSchema import BuildingSchema

from src.util.constant import RESPONSE
from src.util.common import get_exception_http

class FindByNameAndFlatBuildingService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = FindByNameAndFlatBuildingRepository(db)
        self.schema = BuildingSchema()

    # @override
    # @method - Consulta un edificio por su nombre y piso
    # @parameter - data - Json con nombre y piso del edificio
    # @return - Building
    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element= None
        finally:
            if element == None:
                raise get_exception_http(RESPONSE['building']['get']['find_by_name_and_flat']['error']['default'])
        return element