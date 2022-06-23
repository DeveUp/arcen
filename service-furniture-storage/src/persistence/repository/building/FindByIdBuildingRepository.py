"""
    @name - FindByIdBuildingRepository
    @description - Repositorio para consultar un edificio por su pk
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

class FindByIdBuildingRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Consulta un edificio por su pk
    # @parameter - data - Json con el pk del edificio
    # @return - Any
    def execute(self, data:dict):
        id = int(data[DATABASE['table']['building']['pk']])
        return self.db.query(Building).filter(Building.id == id).first()
       