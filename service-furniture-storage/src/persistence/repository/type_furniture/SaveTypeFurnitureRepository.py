"""
    @name - SaveTypeFurnitureRepository
    @description - Repositorio para registrar un tipo de mueble
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.model.entity.TypeFurniture import TypeFurniture

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class SaveTypeFurnitureRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Registra un tipo de mueble
    # @parameter - data - Json con el tipo de mueble a registrar
    # @return - TypeFurniture
    def execute(self, data:dict):
        element = TypeFurniture(**dict(data[DATABASE['table']['type_furniture']['name']]))
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element