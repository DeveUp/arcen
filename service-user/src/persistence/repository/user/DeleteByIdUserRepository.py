"""
    @name - DeleteByIdUserRepository
    @description - Repositorio para eliminar un user
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_USER

class DeleteByIdUserRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Elimina un user por su pk
    # @parameter - data - Json con el pk del user
    # @return - Boolean
    def execute(self, data:dict):
        element = data[COLUMN_USER]
        self.db.delete(element)
        self.db.commit()
        return True