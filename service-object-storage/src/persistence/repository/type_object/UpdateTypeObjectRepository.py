"""
    @name - UpdateTypeObjectRepository
    @description - Repositorio para actualizar un tipo de objecto por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.model.entity.TypeObject import TypeObject

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class UpdateTypeObjectRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Actualiza un tipo de objecto por su pk
    # @parameter - data - Json con el pk del tipo de objecto y el tipo de objecto a actualizar
    # @return - TypeObject
    def execute(self, data:dict):
        id = data[DATABASE['table']['type_object']['pk']]
        element = data[DATABASE['table']['type_object']['name']]
        element = self.diff(element, self.db.query(TypeObject).get(id))
        self.db.commit()
        self.db.refresh(element)
        return element
    
    # @method - Actualiza la diferencia entre dos tipos de objectos
    # @parameter - element_new - Json con el tipo de objecto nuevo
    # @parameter - element - Json con la informacion bd
    # @return - TypeObject
    def diff(self, element_new, element:TypeObject):
        element.name = element_new.name
        element.height = element_new.height
        element.width = element_new.width
        element.depth = element_new.depth
        return element