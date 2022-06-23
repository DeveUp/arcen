"""
    @name - SaveBuildingRepository
    @description - Repositorio para registrar un edificio
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

class SaveBuildingRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Registra un edificio
    # @parameter - data - Json con el edificio a registrar
    # @return - Building
    def execute(self, data:dict):
        element = Building(**dict(data[DATABASE['table']['building']['name']]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element