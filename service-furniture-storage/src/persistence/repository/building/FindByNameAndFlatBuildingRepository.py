"""
    @name - FindByNameAndFlatBuildingRepository
    @description - Repositorio para consultar un edificio por su nombre y piso
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.model.entity.Building import Building

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class FindByNameAndFlatBuildingRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Consulta un edificio por su nombre y piso
    # @parameter - data - Json con el nombre y piso del edificio
    # @return - Any
    def execute(self, data:dict):
        name = data[DATABASE['table']['building']['column'][1]]
        flat = data[DATABASE['table']['building']['column'][4]]
        return self.db.query(Building).filter(Building.name == name).filter(Building.flat == flat).first()