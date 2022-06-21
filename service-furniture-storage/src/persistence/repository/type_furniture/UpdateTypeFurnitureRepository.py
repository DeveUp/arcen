"""
    @name - UpdateTypeFurnitureRepository
    @description - Repositorio para actualizar un tipo de mueble por su pk
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

class UpdateTypeFurnitureRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db =  db

    # @override
    # @method - Actualiza un tipo de mueble por su pk
    # @parameter - data - Json con el pk del tipo de mueble y el tipo de mueble a actualizar
    # @return - TypeFurniture
    def execute(self, data:dict):
        id = data[DATABASE['table']['type_furniture']['pk']]
        element = data[DATABASE['table']['type_furniture']['name']]
        element = self.diff(element, self.db.query(TypeFurniture).get(id))
        self.db.commit()
        self.db.refresh(element)
        return element
    
    # @parameter - element_new - Json con el tipo de mueble nuevo
    # @parameter - element - Json con la informacion bd
    # @return - TypeFurniture
    def diff(self, element_new, element:TypeFurniture):
        element.number_type_furniture = element_new.number_type_furniture
        element.count_rack = element_new.count_rack
        element.count_row = element_new.count_row
        element.depth = element_new.depth
        element.height = element_new.height
        element.width = element_new.width
        return element