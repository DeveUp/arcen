"""
    @name - UpdateFurnitureRepository
    @description - Repositorio para actualizar un mueble por su pk
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

class UpdateFurnitureRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Actualiza un mueble por su pk
    # @parameter - data - Json con el pk del mueble y el mueble a actualizar
    # @return - Furniture
    def execute(self, data:dict):
        id = data[DATABASE['table']['furniture']['pk']]
        element = data[DATABASE['table']['furniture']['name']]
        element = self.diff(element, self.db.query(Furniture).get(id))
        self.db.commit()
        self.db.refresh(element)
        return element
    
    # @parameter - element_new - Json con el mueble nuevo
    # @parameter - element - Json con la informacion bd
    # @return - Furniture
    def diff(self, element_new, element:Furniture):
        element.id_block = element_new.id_block
        element.id_type_furniture = element_new.id_type_furniture
        element.number_furniture = element_new.number_furniture
        return element