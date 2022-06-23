"""
    @name - UpdateBuildingRepository
    @description - Repositorio para actualizar un edificio por su pk
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

class UpdateBuildingRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Actualiza un edificio por su pk
    # @parameter - data - Json con el pk del edificio y el edificio a actualizar
    # @return - Building
    def execute(self, data:dict):
        id = data[DATABASE['table']['building']['pk']]
        element = data[DATABASE['table']['building']['name']]
        element = self.diff(element, self.db.query(Building).get(id))
        self.db.commit()
        self.db.refresh(element)
        return element

    # @method - Actualiza la diferencia entre dos edificios
    # @parameter - element_new - Json con el edificio nuevo
    # @parameter - element - Json con la informacion bd
    # @return - Building
    def diff(self, element_new, element:Building):
        element.name = element_new.name
        element.name_area = element_new.name_area
        element.cellar = element_new.cellar
        element.flat = element_new.flat
        return element