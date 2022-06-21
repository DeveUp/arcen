"""
    @name - DeleteByIdFurnitureRepository
    @description - Repositorio para eliminar un mueble
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class DeleteByIdFurnitureRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Elimina un mueble por su pk
    # @parameter - data - Json con el pk del mueble
    # @return - Boolean
    def execute(self, data:dict):
        element = data[DATABASE['table']['furniture']['name']]
        self.db.delete(element)
        self.db.commit()
        return True