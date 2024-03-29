"""
    @name - DeleteByIdSubObjectRepository
    @description - Repositorio para eliminar un subobjeto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy.orm import Session

from src.persistence.repository.IRepository import IRepository

from src.util.constant import DATABASE

class DeleteByIdSubObjectRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Elimina un subobjeto por su pk
    # @parameter - data - Json con el pk del objeto
    # @return - Boolean
    def execute(self, data:dict):
        element = data[DATABASE['table']['subobject']['name']]
        self.db.delete(element)
        self.db.commit()
        return True