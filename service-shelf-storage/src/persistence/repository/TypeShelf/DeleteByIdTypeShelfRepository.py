"""
    @name - DeleteByIdTypeShelfRepository
    @description - Repositorio para eliminar un type shelf
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_TYPE_SHELF

class DeleteByIdTypeShelfRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Elimina un type shelf por su pk
    # @parameter - data - Json con el pk del type shelf
    # @return - Boolean
    def execute(self, data:dict):
        element = data[COLUMN_TYPE_SHELF]
        self.db.delete(element)
        self.db.commit()
        return True