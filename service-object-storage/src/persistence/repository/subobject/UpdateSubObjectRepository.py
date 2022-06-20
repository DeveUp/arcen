"""
    @name - UpdateSubObjectRepository
    @description - Repositorio para actualizar un subobjeto por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.model.entity.SubObject import SubObject

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class UpdateSubObjectRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Actualiza un subobjeto por su pk
    # @parameter - data - Json con el pk del subobjeto y el subobjeto a actualizar
    # @return - SubObject
    def execute(self, data:dict):
        id = data[DATABASE['table']['subobject']['pk']]
        element = data[DATABASE['table']['subobject']['name']]
        element = self.diff(element, self.db.query(SubObject).get(id))
        self.db.commit()
        self.db.refresh(element)
        return element

    # @method - Actualiza la diferencia entre dos objectos
    # @parameter - element_new - Json con el objecto nuevo
    # @parameter - element - Json con la informacion bd
    # @return - Object
    def diff(self, element_new, element:SubObject):
        element.number = element_new.number
        element.box = element_new.box
        return element