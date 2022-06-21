"""
    @name - SaveFurnitureRepository
    @description - Repositorio para registrar un mueble
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.model.entity.Furniture import Furniture

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class SaveFurnitureRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Registra un mueble
    # @parameter - data - Json con el mueble a registrar
    # @return - Furniture
    def execute(self, data:dict):
        element = Furniture(**dict(data[DATABASE['table']['furniture']['name']]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element