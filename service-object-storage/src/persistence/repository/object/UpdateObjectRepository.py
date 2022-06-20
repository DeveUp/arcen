"""
    @name - UpdateObjectRepository
    @description - Repositorio para actualizar un objecto por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.model.entity.Object import Object

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class UpdateObjectRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db:Session):
        self.db = db

    # @override
    # @method - Actualiza un objecto por su pk
    # @parameter - data - Json con el pk del objecto y el objecto a actualizar
    # @return - Object
    def execute(self, data:dict):
        id = data[DATABASE['table']['object']['pk']]
        element = data[DATABASE['table']['object']['name']]
        element = self.diff(element, self.db.query(Object).get(id))
        self.db.commit()
        self.db.refresh(element)
        return element

    # @method - Actualiza la diferencia entre dos objectos
    # @parameter - element_new - Json con el objecto nuevo
    # @parameter - element - Json con la informacion bd
    # @return - Object
    def diff(self, element_new, element:Object):
        element.id_sub_object = element_new.id_sub_object
        element.id_type_object = element_new.id_type_object
        return element