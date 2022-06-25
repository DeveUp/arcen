"""
    @name - DeleteByIdShelfRepository
    @description - Repositorio para eliminar un shelf
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_SHELF

class DeleteByIdShelfRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Elimina un shelf por su pk
    # @parameter - data - Json con el pk del shelf
    # @return - Boolean
    def execute(self, data:dict):
        element = data[COLUMN_SHELF]
        self.db.delete(element)
        self.db.commit()
        return True