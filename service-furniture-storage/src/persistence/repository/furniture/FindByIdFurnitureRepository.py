"""
    @name - FindByIdFurnitureRepository
    @description - Repositorio para consultar un mueble por su pk
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

class FindByIdFurnitureRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Consulta un mueble por su pk
    # @parameter - data - Json con el pk del mueble
    # @return - Any
    def execute(self, data:dict):
        id = int(data[DATABASE['table']['furniture']['pk']])
        return self.db.query(Furniture).filter(Furniture.id == id).first()
       