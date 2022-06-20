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
    # @return - Boolean
    def execute(self, data:dict):
        id = data[DATABASE['table']['object']['pk']]
        element = data[DATABASE['table']['object']['name']]
        element = self.db.query(Object).get(id)
        self.db.commit()
        self.db.refresh(element)
        return element