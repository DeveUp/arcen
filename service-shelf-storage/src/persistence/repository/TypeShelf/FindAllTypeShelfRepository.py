"""
    @name - FindAllTypeShelfRepository
    @description - Repositorio para consultar todas los type shelf
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.model.entity.TypeShelf import TypeShelf
from src.persistence.repository.IRepository import IRepository

class FindAllTypeShelfRepository(IRepository):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.db = db

    # @override
    # @method - Todas los type shelf
    # @parameter - data - No aplica
    # @return - list
    def execute(self, data:dict):
        return self.db.query(TypeShelf).all()